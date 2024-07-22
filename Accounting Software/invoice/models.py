from django.db import models
from decimal import Decimal
from COA.models import COA
from Journal_Entries.models import *

class InvoiceEntry(models.Model):
    STATUS_CHOICES = [
        ('Paid', 'Paid'),
        ('Pending', 'Pending'),
        ('Partially-Paid', 'Partially-Paid'),
    ]
    invoice_date = models.DateField()
    due_date = models.DateField()
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='invoices')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='invoices')
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))
    paid_amount = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    grand_total_taxed = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))

    def __str__(self):
        return f"Invoice {self.id} - {self.customer.name}"

    def save(self, *args, **kwargs):
        # Calculate total_amount and grand_total_taxed before saving the invoice
        if self.pk is not None:
            self.total_amount = sum(line.amount_before_tax for line in self.line_products.all())
            self.grand_total_taxed = sum(line.amount_after_tax for line in self.line_products.all())
            
        super().save(*args, **kwargs)
        
        # Create Journal Entries only when the invoice is created (not updated)
        if not hasattr(self, '_create_journal_entries_done') or not self._create_journal_entries_done:
            self.create_journal_entries()
            self._create_journal_entries_done = True


    def create_journal_entries(self):
        # Create Journal Entry
        journal_entry = JournalEntries.objects.create(
            date=self.invoice_date,
            reference=f"INV-{self.id}",
            posted=True
        )
        
        # Get COA accounts by IDs
        try:
            receivables_account = COA.objects.get(id=22)  # Accounts Receivable (A/R)
            income_account = COA.objects.get(id=21)  # Sales of Product Income
            gst_account = COA.objects.get(id=24)  # Output GST
        except COA.DoesNotExist as e:
            # Log the missing COA accounts for debugging
            print(f"Error: {str(e)}")
            return

        # Create Journal Entry Lines
        JournalEntryLines.objects.create(
            journal_entry=journal_entry,
            account=receivables_account,
            description='Receivables for Invoice',
            debit=self.grand_total_taxed,
            
            customer=self.customer,
            project=self.project
        )

        JournalEntryLines.objects.create(
            journal_entry=journal_entry,
            account=income_account,
            description='Income from Invoice',
            
            credit=self.total_amount,
            customer=self.customer,
            project=self.project
        )

        JournalEntryLines.objects.create(
            journal_entry=journal_entry,
            account=gst_account,
            description='GST on Invoice',
            
            credit=self.grand_total_taxed - self.total_amount,
            customer=self.customer,
            project=self.project
        )


class InvoiceEntryLineProduct(models.Model):
    invoice_entry = models.ForeignKey(InvoiceEntry, on_delete=models.CASCADE, related_name='line_products')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
    quantity = models.DecimalField(max_digits=10, decimal_places=0)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    amount_before_tax = models.DecimalField(max_digits=10, decimal_places=2, editable=True, default=Decimal('0.00'))
    taxable = models.BooleanField(default=False)
    gst_percentage = models.DecimalField(max_digits=5, decimal_places=2, default=0, null=True, blank=True)
    amount_after_tax = models.DecimalField(max_digits=10, decimal_places=2, editable=True, default=Decimal('0.00'))

    def __str__(self):
        return f"Product Line {self.id} - {self.product.name}"

    def save(self, *args, **kwargs):
        # Set unit_price from product if not set
        if not self.unit_price and self.product:
            self.unit_price = self.product.price

        # Calculate amounts
        self.amount_before_tax = self.quantity * self.unit_price
        if self.taxable:
            self.amount_after_tax = self.amount_before_tax + (self.amount_before_tax * self.gst_percentage / 100)
        else:
            self.amount_after_tax = self.amount_before_tax

        super().save(*args, **kwargs)
