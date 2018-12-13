
class DocBuilder(object):
    @staticmethod
    def analyzer_object(obj):
        info = "\033[38;2;186;225;255m"
        class_name_color = "\033[38;2;186;255;201m"
        property_color = "\033[38;2;241;203;255m"
        type_color= "\033[38;2;255;132;132m"
        methods_color = "\033[38;2;253;204;0m"
        end = "\033[39m"
        pure_class_name=str(obj.get('class name', None))
        class_name = class_name_color+pure_class_name+end
        if class_name is None:
            raise Exception("A class don't have a name")
        ret = ""
        ret += "\n"+info+"Doc for " + class_name+end+"\n"

        '''constructors'''
        constructors = obj.get('constructors', None)
        if constructors is not None:
            ret += "\n"+info+"Constructors"+end
            for i in constructors:
                if i is not None:
                    params = i.get('params', None)
                    description = str(i.get('description', None))
                    ret += "\n\n"+class_name+"("
                    f = True
                    for p in params:
                        ret += ("" if f else ", ")+p.get('name', '')
                        f = False
                    ret += ")"
                    for p in params:
                        ret += "\n\t"+p.get("name", "No_Name")+": "\
                               + p.get("type", "object")+", "+p.get("description", "")
                    if description is not None:
                        ret += "\n\tdescription: "+description
        '''property'''
        prop = obj.get('property', None)
        if prop is not None:
            ret += "\n\n"+info+"Property"+end+"\n"
            maxlength = 0
            for i in prop:
                if i is not None:
                    name = str(i.get("name", ""))
                    if maxlength < len(name):
                        maxlength = len(name)
            maxlength += 3
            for i in prop:
                if i is not None:
                    name = str(i.get("name", ""))
                    ty = type_color+str(i.get("type", ""))+end
                    description = str(i.get("description", ""))
                    ret += "\n"+class_name+"."+property_color+name+end+(" "*(maxlength-len(name)))
                    ret += "-> " + ty+", "
                    f = True
                    for dt in description.split("\n"):
                        ret += "" if f else "\n"+" "*len(pure_class_name+"."+name+(" "*(maxlength+3-len(name))))
                        ret += dt
                        f = False
        '''methods'''
        methods = obj.get('methods', None)
        if methods is not None:
            ret += "\n\n"+info+"Methods"+end
            for i in methods:
                if i is not None:
                    name = methods_color+i.get("name", "")+end
                    params = i.get("params", "")
                    description = i.get("description", "")
                    return_type = i.get("return_type", "")
                    ret += "\n\n" + class_name + "."+name+"("
                    f = True
                    for p in params:
                        ret += ("" if f else ", ") + property_color + p.get('name', '') + end
                        f = False
                    ret += ")"
                    for p in params:
                        ret += "\n\t"+property_color+p.get("name", "No_Name")+end+": "\
                               +(type_color if p.get("type", "object") != pure_class_name else class_name_color) \
                               + p.get("type", "object")+end+", "+p.get("description", "")
                    if description is not None:
                        ret += "\n\tdescription: " + description
                    if return_type is not None and return_type != "None":
                        ret += "\n\treturn: " + return_type
        '''events'''
        events = obj.get('events', None)
        if events is not None:
            ret += "\n\n"+info+"Events"+end
            for i in events:
                if i is not None:
                    name = i.get("name", "")
                    params = i.get("params", "")
                    description = i.get("description", "")
                    ret += "\n\n" + class_name + "."+ methods_color + name+"("+end
                    f = True
                    for p in params:
                        ret += ("" if f else ", ") + property_color+p.get('name', '')+end
                        f = False
                    ret += ")"
                    for p in params:
                        ret += "\n\t"+property_color+p.get("name", "No_Name")+end+": "\
                               +(type_color if p.get("type", "object") != pure_class_name else class_name_color) \
                               + p.get("type", "object")+end+", "+p.get("description", "")
                    if description is not None:
                        ret += "\n\tdescription: " + description
        return ret+"\n"

