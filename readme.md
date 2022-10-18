## 01平安证券app项目
1. 通过关键字驱动的方式，可以实现以下功能：
   - 股票：买入卖出、添加/取消收藏、查看详情、股票行情等
   - 基金: 定投、继续购买、买入、赎回、详情查看、添加/取消 自选 等
## 02 项目架构
**1.**  PoObject 封装主要组成元素
- Page对象:完成对页面的封装
- Driver对象:完成对web、android、ios、接口的驱动
- 测试用例:调用Page对象实现业务并断言
- 数据封装:配置文件和数据驱动
- Utils:其他功能封装，改进原生框架不足

**2.** 测试数据的数据驱动
- 基本用法：@pytest.mark.parametrize("value1, value2", yaml.safe_load(open("file_name")))
def test_value(self, value1, value2):
    pass
- 启动参数caps
- 登录用户名、密码
- uuid(多并发自动化用到) 
   
**3.** 测试步骤数据驱动
- 元素定位方式：by
- 元素:locator
- 操作方法：click、send、text、clear、eles
- assert 断言

**4.** 自动化异常处理机制
- 弹框处理
- 操作前登录处理

**5.** 通用测试用例封装
- 初始化driver
- 关闭退出driver
- 返回上一层

**6.** 装饰器优化
- 弹框处理
- 登录
- 日志输出
- 截屏
