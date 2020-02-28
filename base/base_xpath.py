
class Xpath:

    def make_xpath_with_feature(self,loc):
        feature_start = "//*["
        feature_end = "]"
        feature_middol = ""
        if isinstance(loc,str):
            feature_middol = self.make_xpath_with_until_feature(loc)
        else:
            for i in loc:
                feature_middol += self.make_xpath_with_until_feature(i) + "and"
            feature_middol = feature_middol.rstrip("and")
        return feature_start + feature_middol + feature_end

    def make_xpath_with_until_feature(self,loc):
            args = loc.split(",")
            num = len(args)
            key_index = 0
            value_index = 1
            option_index = 2
            feature = ""
            if num == 2:
                feature="contains（@" + args[key_index] + ",'" + args[value_index] + "')"
            elif num == 3:
                if args[option_index] == "0":
                      feature = "contains（@" + args[key_index] + ",'" + args[value_index] + "')"
                elif args[option_index] == "1":
                      feature = "@" + args[key_index] + "='" + args[value_index] + "'"
            return feature
