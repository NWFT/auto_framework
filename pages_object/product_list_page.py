from pagee_elements_locator.product_list_page_locator import ProductListLocators as loc
from pages_object.base_page import BasePage

class ProductListPage(BasePage):

    def click_to_product_detail_page(self):
        """
        click a item to detail page
        :return:
        """
        self.click_element(loc.product_list_loc, "ProductListPage_Click-to-detail")