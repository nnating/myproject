# @Time     :2021/11/17 11:19
# @Author   :dengyuting
# @File     :test_views.py

from django.test import TestCase
from django.test import Client

from storage.models import Companys


class CompanysTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Set up data for the whole TestCase
        # cls.company = Companys.objects.create(company_name="unit test company", company_logo="unit test logo", system_name="unit test system name")
        pass

    def test1(self):
        # Some test using self.job
        pass


    def test_detail(self):
        # 使用 TestCase.self.client 作为 HTTP Client:
        response = self.client.get('/companys/6')
        self.assertEqual(response.status_code, 200)
        print(response)

        # job = response.context['job']
        # self.assertEqual(job.job_name, JobTests.job.job_name)