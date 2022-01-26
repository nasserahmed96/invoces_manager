from src.DataAccessObjects.DashboardDao import DashboardDao
import datetime


class DashboardDaoTesting:
    def __init__(self):
        self.dashboard_dao = DashboardDao()

    def test_get_invoices_in_month(self):
        print('Number of invoices in current month: ',
              self.dashboard_dao.get_invoices_in_month(datetime.datetime.now().date().strftime('%m')))

    def run_tests(self):
        self.test_get_invoices_in_month()


if __name__ == '__main__':
    dashboard_testing = DashboardDaoTesting()
    dashboard_testing.run_tests()