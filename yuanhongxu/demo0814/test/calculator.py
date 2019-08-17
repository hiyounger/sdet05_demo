# coding:utf-8


class calculator_bt():

    def __init__(self,driver):
        self.driver=driver

    @property
    def bt1(self):
        ele=self.driver.find_element_by_id("com.miui.calculator:id/btn_1_s")
        return ele

    @property
    def bt2(self):
        ele = self.driver.find_element_by_id("com.miui.calculator:id/btn_2_s")
        return ele

    @property
    def bt3(self):
        ele = self.driver.find_element_by_id("com.miui.calculator:id/btn_3_s")
        return ele

    @property
    def bt4(self):
        ele = self.driver.find_element_by_id("com.miui.calculator:id/btn_4_s")
        return ele

    @property
    def bt5(self):
        ele = self.driver.find_element_by_id("com.miui.calculator:id/btn_5_s")
        return ele

    @property
    def bt6(self):
        ele = self.driver.find_element_by_id("com.miui.calculator:id/btn_6_s")
        return ele

    @property
    def bt7(self):
        ele = self.driver.find_element_by_id("com.miui.calculator:id/btn_7_s")
        return ele

    @property
    def bt8(self):
        ele = self.driver.find_element_by_id("com.miui.calculator:id/btn_8_s")
        return ele

    @property
    def bt9(self):
        ele = self.driver.find_element_by_id("com.miui.calculator:id/btn_9_s")
        return ele

    @property
    def bt_plus(self):
        ele = self.driver.find_element_by_id("com.miui.calculator:id/btn_plus_s")
        return ele

    @property
    def bt_minus(self):
        ele = self.driver.find_element_by_id("com.miui.calculator:id/btn_minus_s")
        return ele

    @property
    def bt_mul(self):
        ele = self.driver.find_element_by_id("com.miui.calculator:id/btn_mul_s")
        return ele

    @property
    def bt_div(self):
        ele = self.driver.find_element_by_id("com.miui.calculator:id/btn_div_s")
        return ele

    @property
    def bt_equal(self):
        ele = self.driver.find_element_by_id("com.miui.calculator:id/btn_equal_s")
        return ele

    @property
    def bt_result(self):
        ele = self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/miui.view.ViewPager/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.HorizontalScrollView[3]/android.widget.LinearLayout/android.widget.TextView[2]")
        return ele

    @property
    def bt_c(self):
        ele = self.driver.find_element_by_id("com.miui.calculator:id/btn_c_s")
        return ele