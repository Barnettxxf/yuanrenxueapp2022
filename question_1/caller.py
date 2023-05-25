import os

import jpype
import array

jar_path = os.path.abspath('.') + '/question_1/sign.jar'  # 获取jar包绝对路径
jvmPath = jpype.getDefaultJVMPath()
jpype.startJVM(jvmPath, '-ea',
               '-Djava.class.path=%s' % jar_path)  # 加载java虚拟机，第一个参数是Java的jdk安装位置，可以通过env | prep JAVA_HOME来查看；第二个参数仿照例子来写；第三个参数为jar包的绝对路径；
java_class = jpype.JClass('com.yuanrenxue.application.Sign')  # 通过输入类名称来获取指定的Java类
string_class = jpype.JClass('java.lang.String')
string = string_class('page=1216488369808')
result = java_class().sign(string)  # 通过函数名称来调用该类的指定函数
print(result)
jpype.shutdownJVM()
