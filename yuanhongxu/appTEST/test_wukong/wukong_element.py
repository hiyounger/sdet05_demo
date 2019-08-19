#coding:utf-8


class WuKong():

    def __init__(self,driver):
        self.driver=driver

    #待办页面按钮
    @property
    def ele_db_bt(self):
        ele=self.driver.find_element_by_xpath('//android.widget.Image[@content-desc="F7FBCsAvZcAAAAAElFTkSuQmCC"]')
        return ele

    #待审核回款按钮
    @property
    def ele_dshhk(self):
        ele=self.driver.find_element_by_xpath('//android.view.View[@content-desc=" 待审核回款"]')
        return ele

    #待审核回款的第一个
    @property
    def ele_dshhk_first(self):
        ele=self.driver.find_elements_by_xpath('//android.view.View[@content-desc=*]')
        for i in ele:
            return i

    #回款详情审核状态待审核
    @property
    def ele_hkxqzt(self):
        ele = self.driver.find_element_by_xpath('//android.view.View[@content-desc="待审核"]')
        return ele

    #待审核下拉框
    @property
    def ele_dsh_xlk(self):
        ele = self.driver.find_element_by_xpath('//android.view.View[@content-desc="待审核"]')
        return ele

    #已审核下拉框
    @property
    def ele_ysh_xlk(self):
        ele = self.driver.find_element_by_xpath('//android.view.View[@content-desc="已审核"]')
        return ele

    #回款详情审核状态待审核
    @property
    def ele_hkxqzt_shjj(self):
        ele = self.driver.find_element_by_xpath('//android.view.View[@content-desc="审核拒绝"]')
        return ele

    #拒绝回款客户信息
    @property
    def ele_dshhk_yjj(self):
        ele = self.driver.find_element_by_xpath('//android.view.View[@content-desc="2456 1111.00元 客户名称 袁袁 已拒绝 回款日期 2019-08-08"]')
        return ele

    #商机图标
    @property
    def ele_sj(self):
        ele = self.driver.find_element_by_xpath('//android.widget.Image[@content-desc="k4ZqxtoPJHoXrYIMdhesg3P8BOiMto2eySrQAAAAASUVORK5CYII="]')
        return ele

    #新增商机按钮
    @property
    def ele_xzsj(self):
        ele = self.driver.find_element_by_xpath('//android.webkit.WebView[@content-desc="crm_app"]/android.view.View/android.view.View/android.view.View[1]/android.view.View[2]/android.widget.Button[2]')
        return ele

    #商机名称
    @property
    def ele_sjmc(self):
        ele = self.driver.find_element_by_xpath('//android.webkit.WebView[@content-desc="crm_app"]/android.view.View/android.view.View/android.view.View[2]/android.view.View[1]/android.view.View/android.widget.EditText')
        return ele

    #客户名称
    @property
    def ele_khmc(self):
        ele = self.driver.find_element_by_xpath('//android.view.View[@content-desc="客户名称 "]/android.view.View/android.view.View[2]')
        return ele

    #选择客户
    @property
    def ele_choose_kh(self):
        ele = self.driver.find_element_by_xpath('//android.view.View[@content-desc="周"]')
        return ele

    #返回
    @property
    def ele_return(self):
        ele = self.driver.find_element_by_xpath('(//android.widget.Button[@content-desc=" "])[2]')
        return ele

    #商机组状态
    @property
    def ele_sjzzt(self):
        ele = self.driver.find_element_by_xpath('//android.view.View[@content-desc="商机状态组 "]/android.view.View')
        return ele

    #选择商机组
    @property
    def ele_choose_sjz(self):
        ele = self.driver.find_element_by_xpath('//android.view.View[@content-desc="系统默认"]')
        return ele

    #商机阶段
    @property
    def ele_sjjd(self):
        ele = self.driver.find_element_by_xpath('//android.view.View[@content-desc="商机阶段 "]/android.view.View')
        return ele

    #选择商机阶段
    @property
    def ele_choose_sjjd(self):
        ele = self.driver.find_element_by_xpath('//android.view.View[@content-desc="验证客户"]')
        return ele

    #商机金额
    @property
    def ele_sjje(self):
        ele = self.driver.find_element_by_xpath('//android.widget.EditText[@content-desc="元"]')
        return ele

    #保存商机
    @property
    def ele_bc(self):
        ele = self.driver.find_element_by_xpath('//android.widget.Button[@content-desc="保存"]')
        return ele

    #商机详情
    @property
    def ele_sjnr(self):
        ele = self.driver.find_element_by_xpath('(//android.view.View[@content-desc="学习"])[2]')
        return ele

    #商机列表里的商机金额
    @property
    def ele_sj_sjje(self):
        ele = self.driver.find_element_by_xpath('(//android.view.View[@content-desc="145.00"])[1]')
        return ele

