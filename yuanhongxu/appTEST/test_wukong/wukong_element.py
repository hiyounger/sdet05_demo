# coding:utf-8
import time
from . import config


class WuKong():

    def __init__(self, driver):
        self.driver = driver

    def write(self, xpath):
        chishu = int(config.wait_max_time / config.wait_time)
        for i in range(chishu):
            try:
                ele = self.driver.find_element_by_xpath(xpath)
                # print ("在第%s秒找到这个控件"%(i/2))
                return ele
            except:
                time.sleep(config.wait_time)
                if i == (chishu - 1):
                    print("无法获取xpath为%s的控件" % xpath)
                    return None

    # 待办页面按钮
    @property
    def ele_db_bt(self):
        # try:
        #     ele=self.driver.find_element_by_xpath('//android.widget.Image[@content-desc="F7FBCsAvZcAAAAAElFTkSuQmCC"]')
        # except:
        #     time.sleep(10)
        #     ele = self.driver.find_element_by_xpath('//android.widget.Image[@content-desc="F7FBCsAvZcAAAAAElFTkSuQmCC"]')
        xpath = '//android.widget.Image[@content-desc="F7FBCsAvZcAAAAAElFTkSuQmCC"]'
        ele = self.write(xpath)
        return ele

    # 待审核回款按钮
    @property
    def ele_dshhk(self):
        # ele=self.driver.find_element_by_xpath('//android.view.View[@content-desc=" 待审核回款"]')
        xpath = '//android.view.View[@content-desc=" 待审核回款"]'
        ele = self.write(xpath)
        return ele

    # 待审核回款的第一个
    @property
    def ele_dshhk_first(self):
        ele = self.driver.find_elements_by_xpath('//android.view.View[@content-desc=*]')
        for i in ele:
            return i

    # 回款详情审核状态待审核
    @property
    def ele_hkxqzt(self):
        # ele = self.driver.find_element_by_xpath('//android.view.View[@content-desc="待审核"]')
        xpath = '//android.view.View[@content-desc="待审核"]'
        ele = self.write(xpath)
        return ele

    # 待审核下拉框
    @property
    def ele_dsh_xlk(self):
        # ele = self.driver.find_element_by_xpath('//android.view.View[@content-desc="待审核"]')
        xpath = '//android.view.View[@content-desc="待审核"]'
        ele = self.write(xpath)
        return ele

    # 已审核下拉框
    @property
    def ele_ysh_xlk(self):
        # ele = self.driver.find_element_by_xpath('//android.view.View[@content-desc="已审核"]')
        xpath = '//android.view.View[@content-desc="已审核"]'
        ele = self.write(xpath)
        return ele

    # 回款详情审核状态待审核
    @property
    def ele_hkxqzt_shjj(self):
        # ele = self.driver.find_element_by_xpath('//android.view.View[@content-desc="审核拒绝"]')
        xpath = '//android.view.View[@content-desc="审核拒绝"]'
        ele = self.write(xpath)
        return ele

    # 拒绝回款客户信息
    @property
    def ele_dshhk_yjj(self):
        # ele = self.driver.find_element_by_xpath('//android.view.View[@content-desc="2456 1111.00元 客户名称 袁袁 已拒绝 回款日期 2019-08-08"]')
        xpath = '//android.view.View[@content-desc="2456 1111.00元 客户名称 袁袁 已拒绝 回款日期 2019-08-08"]'
        ele = self.write(xpath)
        return ele

    # 商机图标
    @property
    def ele_sj(self):
        # ele = self.driver.find_element_by_xpath('//android.widget.Image[@content-desc="k4ZqxtoPJHoXrYIMdhesg3P8BOiMto2eySrQAAAAASUVORK5CYII="]')
        xpath = '//android.widget.Image[@content-desc="k4ZqxtoPJHoXrYIMdhesg3P8BOiMto2eySrQAAAAASUVORK5CYII="]'
        ele = self.write(xpath)
        return ele

    # 新增商机按钮
    @property
    def ele_xzsj(self):
        # ele = self.driver.find_element_by_xpath(
        #     '//android.webkit.WebView[@content-desc="crm_app"]/android.view.View/android.view.View/android.view.View[1]/android.view.View[2]/android.widget.Button[2]')
        xpath = '//android.webkit.WebView[@content-desc="crm_app"]/android.view.View/android.view.View/android.view.View[1]/android.view.View[2]/android.widget.Button[2]'
        ele = self.write(xpath)
        return ele

    # 商机名称
    @property
    def ele_sjmc(self):
        # ele = self.driver.find_element_by_xpath(
        #     '//android.webkit.WebView[@content-desc="crm_app"]/android.view.View/android.view.View/android.view.View[2]/android.view.View[1]/android.view.View/android.widget.EditText')
        xpath = '//android.webkit.WebView[@content-desc="crm_app"]/android.view.View/android.view.View/android.view.View[2]/android.view.View[1]/android.view.View/android.widget.EditText'
        ele = self.write(xpath)
        return ele

    # 客户名称
    @property
    def ele_khmc(self):
        # ele = self.driver.find_element_by_xpath(
        #     '//android.view.View[@content-desc="客户名称 "]/android.view.View/android.view.View[2]')
        xpath = '//android.view.View[@content-desc="客户名称 "]/android.view.View/android.view.View[2]'
        ele = self.write(xpath)
        return ele

    # 选择客户
    @property
    def ele_choose_kh(self):
        # ele = self.driver.find_element_by_xpath('//android.view.View[@content-desc="周"]')
        xpath = '//android.view.View[@content-desc="周"]'
        ele = self.write(xpath)
        return ele

    # 返回
    @property
    def ele_return(self):
        # ele = self.driver.find_element_by_xpath('(//android.widget.Button[@content-desc=" "])[2]')
        xpath = '(//android.widget.Button[@content-desc=" "])[2]'
        ele = self.write(xpath)
        return ele

    # 商机组状态
    @property
    def ele_sjzzt(self):
        # ele = self.driver.find_element_by_xpath('//android.view.View[@content-desc="商机状态组 "]/android.view.View')
        xpath = '//android.view.View[@content-desc="商机状态组 "]/android.view.View'
        ele = self.write(xpath)
        return ele

    # 选择商机组
    @property
    def ele_choose_sjz(self):
        # ele = self.driver.find_element_by_xpath('//android.view.View[@content-desc="系统默认"]')
        xpath = '//android.view.View[@content-desc="系统默认"]'
        ele = self.write(xpath)
        return ele

    # 商机阶段
    @property
    def ele_sjjd(self):
        # ele = self.driver.find_element_by_xpath('//android.view.View[@content-desc="商机阶段 "]/android.view.View')
        xpath = '//android.view.View[@content-desc="商机阶段 "]/android.view.View'
        ele = self.write(xpath)
        return ele

    # 选择商机阶段——验证客户
    @property
    def ele_choose_sjjd(self):
        # ele = self.driver.find_element_by_xpath('//android.view.View[@content-desc="验证客户"]')
        xpath = '//android.view.View[@content-desc="验证客户"]'
        ele = self.write(xpath)
        return ele

    # 选择商机阶段——谈判审核
    @property
    def ele_choose_tpsh(self):
        # ele = self.driver.find_element_by_xpath('//android.view.View[@content-desc="谈判审核"]')
        xpath = '//android.view.View[@content-desc="谈判审核"]'
        ele = self.write(xpath)
        return ele

    # 商机金额
    @property
    def ele_sjje(self):
        # ele = self.driver.find_element_by_xpath('//android.widget.EditText[@content-desc="元"]')
        xpath = '//android.widget.EditText[@content-desc="元"]'
        ele = self.write(xpath)
        return ele

    # 保存商机
    @property
    def ele_bc(self):
        # ele = self.driver.find_element_by_xpath('//android.widget.Button[@content-desc="保存"]')
        xpath = '//android.widget.Button[@content-desc="保存"]'
        ele = self.write(xpath)
        return ele

    # 商机详情
    @property
    def ele_sjnr(self):
        # ele = self.driver.find_element_by_xpath('(//android.view.View[@content-desc="学习"])[2]')
        xpath = '(//android.view.View[@content-desc="学习"])[1]'
        ele = self.write(xpath)
        return ele

    # 商机列表里的商机金额
    @property
    def ele_sj_sjje(self):
        # ele = self.driver.find_element_by_xpath('(//android.view.View[@content-desc="145.00"])[1]')
        xpath = '(//android.view.View[@content-desc="145.00"])[1]'
        ele = self.write(xpath)
        return ele

    # 商机列表里面的商机阶段
    @property
    def ele_sj_sjjd(self):
        # ele = self.driver.find_element_by_xpath('//android.view.View[@content-desc="谈判审核"][1]')
        xpath = '(//android.view.View[@content-desc="谈判审核"])[1]'
        ele = self.write(xpath)
        return ele

    # 我的//android.widget.Image[@content-desc="mfqkAAAAASUVORK5CYII="]
    @property
    def ele_wd(self):
        xpath = '//android.widget.Image[@content-desc="mfqkAAAAASUVORK5CYII="]'
        ele = self.write(xpath)
        return ele

    # 我的页面登陆者用户名//android.view.View[@content-desc="管理员"]
    @property
    def ele_wd_yh(self):
        xpath = '//android.view.View[@content-desc="管理员"]'
        ele = self.write(xpath)
        return ele

    # 我的页面里收到的日志//android.view.View[@content-desc="收到的日志"]
    @property
    def ele_wd_sddrz(self):
        xpath = '//android.view.View[@content-desc="收到的日志"]'
        ele = self.write(xpath)
        return ele

    # 我的日志里面我收到的(//android.view.View[@content-desc="我收到的"])[2]
    @property
    def ele_wd_rz(self):
        xpath = '(//android.view.View[@content-desc="我收到的"])[2]'
        ele = self.write(xpath)
        return ele

    # 我的页面里面的待我审批	//android.view.View[@content-desc="待我审批"]
    @property
    def ele_wd_dwsp(self):
        xpath = '//android.view.View[@content-desc="待我审批"]'
        ele = self.write(xpath)
        return ele

    # 我审批的待我审批的(//android.view.View[@content-desc="待我审批的"])[2]
    @property
    def ele_wd_dwspd(self):
        xpath = '(//android.view.View[@content-desc="待我审批的"])[2]'
        ele = self.write(xpath)
        return ele

    # 办公//android.widget.Image[@content-desc="cGvlN+OnavJN1J8b367y8hQlRbtDOVhgAAAABJRU5ErkJggg=="]
    @property
    def ele_bg(self):
        xpath = '//android.widget.Image[@content-desc="cGvlN+OnavJN1J8b367y8hQlRbtDOVhgAAAABJRU5ErkJggg=="]'
        ele = self.write(xpath)
        return ele

    # 办公里面审批按钮	//android.view.View[@content-desc="审批"]
    @property
    def ele_bg_sp(self):
        xpath = '//android.view.View[@content-desc="审批"]'
        ele = self.write(xpath)
        return ele

    # 办公里面审批图标//android.widget.Image[@content-desc="k7phpPs3wVejHsJniXR6f4kUojFW2j8nkh+jQdagXAIhhpmCRlNfORf05zi6WVaF+6hvoJVY39zOfe+TECM4R5MQI4D4XzgErXD7h3cEAAAAAElFTkSuQmCC"]
    @property
    def ele_bg_sptb(self):
        xpath = '//android.widget.Image[@content-desc="k7phpPs3wVejHsJniXR6f4kUojFW2j8nkh+jQdagXAIhhpmCRlNfORf05zi6WVaF+6hvoJVY39zOfe+TECM4R5MQI4D4XzgErXD7h3cEAAAAAElFTkSuQmCC"]'
        ele = self.write(xpath)
        return ele

    # 审批里面我审批的	//android.view.View[@content-desc="我审批的"]
    @property
    def ele_bg_sp_wsp(self):
        xpath = '//android.view.View[@content-desc="我审批的"]'
        ele = self.write(xpath)
        return ele

    #加班审批//android.view.View[@content-desc="加班审批"]
    @property
    def ele_bg_sp_jbsp(self):
        xpath = '//android.view.View[@content-desc="加班审批"]'
        ele = self.write(xpath)
        return ele

    #旅差报销
    @property
    def ele_bg_sp_lcbx(self):
        xpath = '//android.widget.Image[@content-desc="NZq0kMwAAAAAElFTkSuQmCC"]'
        ele = self.write(xpath)
        return ele

    #借款申请
    @property
    def ele_bg_sp_jksq(self):
        xpath = '//android.widget.Image[@content-desc="8vQt3ekoPAAAAABJRU5ErkJggg=="]'
        ele = self.write(xpath)
        return ele

    #加班原因
    @property
    def ele_bg_sp_jbyy(self):
        xpath = '//android.view.View[@content-desc="加班原因"]'
        ele = self.write(xpath)
        return ele

    #差旅事由
    @property
    def ele_bg_sp_lcsy(self):
        xpath = '//android.view.View[@content-desc="差旅事由"]'
        ele = self.write(xpath)
        return ele

    #借款事由
    @property
    def ele_bg_sp_jksy(self):
        xpath = '//android.view.View[@content-desc="借款事由"]'
        ele = self.write(xpath)
        return ele

    #填写加班原因//android.webkit.WebView[@content-desc="crm_app"]/android.view.View/android.view.View/android.view.View[2]/android.view.View[1]/android.view.View/android.widget.EditText
    @property
    def ele_bg_sp_jbyy_input(self):
        xpath = '//android.webkit.WebView[@content-desc="crm_app"]/android.view.View/android.view.View/android.view.View[2]/android.view.View[1]/android.view.View/android.widget.EditText'
        ele = self.write(xpath)
        return ele

    #填写加班总天数//android.widget.EditText[@content-desc="请输入加班总天数(必填)"]
    @property
    def ele_bg_sp_jbzts_input(self):
        xpath = '//android.widget.EditText[@content-desc="请输入加班总天数(必填)"]'
        ele = self.write(xpath)
        return ele

    #审批人	//android.view.View[@content-desc="+"]
    @property
    def ele_bg_sp_spr(self):
        xpath = '//android.view.View[@content-desc="+"]'
        ele = self.write(xpath)
        return ele

    #选择审批人
    @property
    def ele_bg_sp_spr_choose(self):
        xpath = '//android.view.View[@content-desc="管理员 办公室"]'
        ele = self.write(xpath)
        return ele

    #提示加班总天数不能为空//android.view.View[@content-desc="加班总天数不能为空！"]
    @property
    def ele_bg_sp_ts(self):
        xpath = '//android.view.View[@content-desc="加班总天数不能为空！"]'
        ele = self.write(xpath)
        return ele

    #加班//android.view.View[@content-desc="加班原因不能为空！"]
    @property
    def ele_bg_sp_yyts(self):
        xpath = '//android.view.View[@content-desc="加班原因不能为空！"]'
        ele = self.write(xpath)
        return ele