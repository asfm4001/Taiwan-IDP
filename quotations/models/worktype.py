from django.db import models, transaction

class WorkType(models.Model):
    company = models.ForeignKey('quotations.Company', on_delete=models.CASCADE)
    client = models.ForeignKey('quotations.Client', on_delete=models.CASCADE)

    name = models.CharField('工作項目類型', max_length=50)
    products = models.ManyToManyField('quotations.Product', through='WorkTypeProduct')
    note = models.TextField('備註', blank=True, null=True)

    class Meta:
        verbose_name = '工作項目類型'
        verbose_name_plural = '工作項目類型'

    def __str__(self):
        return self.name

    def clone_from_template(self):
        from quotations.models import Quotation, QuotationProduct, Product, SubProduct

        with transaction.atomic():
            # 1.create new quotation
            new_quotation = Quotation.objects.create(
                company = self.company,
                client = self.client,
                name = self.name,
                status = 'draft',
                note = self.note
            )

            # 2.query qp
            quotation_products = list(
                self.worktypeproduct_set
                .select_related('product')
                .prefetch_related('product__subproducts')
            )

            new_products = []
            new_qp_relations = []
            new_subproducts = []

            # 3.create product
            for qp in quotation_products:
                product = qp.product
                new_products.append(
                    Product(
                        name = product.name,
                        price = product.price
                    )
                )
            # 批次建立product
            Product.objects.bulk_create(new_products)

            # 4. create subproduct, quotationproduct
            for qp, new_product in zip(quotation_products, new_products):
                # create subproduct
                for sp in qp.product.subproducts.all():
                    new_subproducts.append(
                            SubProduct(
                                product=new_product,
                                name=sp.name
                            )
                        )

                # create quotationproduct
                new_qp_relations.append(
                    QuotationProduct(
                        quotation=new_quotation,
                        product=new_product,
                        quantity=qp.quantity
                    )
                )

            # 批次建立subproduct, quotationproduct
            SubProduct.objects.bulk_create(new_subproducts)
            QuotationProduct.objects.bulk_create(new_qp_relations)

            return new_quotation

class WorkTypeProduct(models.Model):
    worktype = models.ForeignKey('quotations.WorkType', on_delete=models.CASCADE)
    product = models.ForeignKey('quotations.Product', on_delete=models.CASCADE)
    quantity = models.IntegerField('數量', default=1)

    def __str__(self):
            return f"{self.worktype} - {self.product} x {self.quantity}"

    @property
    def get_subtotal(self):
        return self.quantity * self.product.price