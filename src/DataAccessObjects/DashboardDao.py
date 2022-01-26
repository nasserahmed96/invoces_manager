from src.DataAccessObjects.DataAccessObject import DataAccessObject


class DashboardDao(DataAccessObject):
    def __init__(self):
        super(DashboardDao, self).__init__()

    def get_invoices_in_month(self, month):
        """
        Get the number of invoices for current month
        :return: Integer represents the number of invoices for the current month
        """
        condition = {
            'column': "strftime('%m', date)",
            'value': month,
            'operator': '=',
            'options': '',
            'logic': '',
            'parameter': 'month'
        }
        invoices = self.select(columns=['COUNT(date) AS invoices_num', ], conditions=[condition, ],
                               table_name='invoices')
        invoices.next()
        return invoices.value('invoices_num')



