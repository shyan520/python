# 8--8.6 将函数存储在模块中###########################################################
def class_info(grade,className,**classInfo):
    c_info = {}
    c_info['年级：'] = grade
    c_info['班级：'] = className
    for k,v in classInfo.items():
        c_info[k] = v
    return c_info
# 此函数的调用，请进入lesson_8_2看