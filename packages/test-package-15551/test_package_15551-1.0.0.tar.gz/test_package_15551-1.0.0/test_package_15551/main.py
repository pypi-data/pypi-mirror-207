class cookie2dict():
    def __init__(self, cookie_str):
        self.cookie_str = cookie_str
    def ToDict(self):
        try:
            cookie_items = self.cookie_str.split(";")
            outdict = {}
            for ci in cookie_items:
                ci_key = ci.split("=")[0].strip()
                ci_value = ci.split("=")[1].strip()
                outdict.update({ci_key:ci_value})
            return outdict
        except Exception as e:
            raise e