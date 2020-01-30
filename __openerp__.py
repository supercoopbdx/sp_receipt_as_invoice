# coding: utf-8
{
    'name': "SP POS XmlReceipt",
    'summary': "Supercoop - Custom POS receipt",
    'description': """
    Displays:
        - The customer name.
        - The "invoice" mention.
    """,
    'author': "Supercoop",
    'website': "http://www.supercoop.fr",
    'category': 'Supercoop',
    'version': '9.0.1.0.1',
    'depends': [
        'point_of_sale',
    ],
    "qweb": [
        'static/src/xml/pos.xml',
    ],
    'data': [
    ],
    'demo': [
    ],
}
