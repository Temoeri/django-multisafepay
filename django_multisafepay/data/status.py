from .base import XmlObject, Price


class Ewallet(XmlObject):
    """
    The EWallet element in the status reply.
    It contains the status code.
    """
    xml_name = 'ewallet'
    xml_fields = (
        'id',
        'status',
        'created',
        'modified',
    )

    def __init__(self, id, status, created, modified):
        self.id = id
        self.status = status
        self.created = created
        self.modified = modified


class PaymentDetails(XmlObject):
    """
    The payment details in the status reply
    """
    xml_name = 'paymentdetails'
    xml_fields = (
        'accountid',
        'accountholdername',
        'externaltransactionid',
    )

    def __init__(self, accountid, accountholdername, externaltransactionid):
        self.accountid = accountid
        self.accountholdername = accountholdername
        self.externaltransactionid = externaltransactionid


class CheckoutData(XmlObject):
    """
    The checkout data in the status reply
    """
    xml_name = 'checkoutdata'
    xml_fields = (
        'shopping-cart',
        'order-adjustment',
        'order-total',
        'custom-fields',
    )

    def __init__(self, order_total, shopping_cart=None, order_adjustment=None, custom_fields=None):
        self.order_total = order_total
        self.shopping_cart = shopping_cart
        self.order_adjustment = order_adjustment
        self.custom_fields = custom_fields

    @classmethod
    def get_class_kwargs(cls, xml):
        """
        :type xml: xml.etree.ElementTree.Element
        """
        return dict(
            order_total=Price.from_xml(xml.find('order-total')),
            order_adjustment=OrderAdjustment.from_xml(xml.find('order-adjustment')),
            shopping_cart=None,
            custom_fields=None,
            # TODO: all other objects are currently ignored. (shopping-cart, custom-fields)
        )


class OrderAdjustment(XmlObject):
    """
    The order adjustment in the CheckoutData of the status reply.
    """
    xml_name = 'order-adjustment'
    xml_fields = (
        'shipping',
        'adjustment-total',
        'total-tax'
    )

    def __init__(self, shipping, adjustment_total, total_tax):
        self.shipping = shipping
        self.adjustment_total = adjustment_total
        self.total_tax = total_tax

    @classmethod
    def get_class_kwargs(cls, xml):
        """
        :type xml: xml.etree.ElementTree.Element
        """
        return dict(
            shipping=None,   # TODO: not implemented
            adjustment_total=Price.from_xml(xml.find('adjustment-total')),
            total_tax=Price.from_xml(xml.find('total-tax')),
        )