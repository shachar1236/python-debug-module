import datetime

# time = datetime.datetime.now()
# time.strftime("%X")

class debug():
    def __init__(self, flieName, Format, pr=True, mode="DEBUG", **values):
        """
        you can put diffrent values in the format like:
        $content for the content of the logging,
        $count for debug time,
        $time for the current time,
        $downline for fo one line down,
        $mode for debug mode (can change mode varibiale),
        $filename for the file name.
        or you can make your own values if you want (can be functions).
        """
        if "$count" in Format:
            self.count = 0
        self.fileName = flieName
        self.values = values
        self.format = Format
        self.pr = pr
        self.mode = mode
        with open(self.fileName + ".txt", "w") as f:
            pass

    def log(self,*text, mode=None):
        content = self.format

        if "$count" in self.format:
            try:
                self.count += 1
            except:
                self.count = 0

            content = content.replace("$count", str(self.count))

        if "$mode" in self.format:
            if mode:
                content = content.replace("$mode", mode)
            else:
                content = content.replace("$mode", str(self.mode))
            
        if "$time" in self.format:
            time = datetime.datetime.now()
            content = content.replace("$time", time.strftime("%X"))
            del time

        if "$filename" in self.format:
            content = content.replace("$filename", str(self.fileName))

        if "$downline" in self.format:
            content = content.replace("$downline", "\n")

        for var in self.values:
            if "$" + var in self.format:
                if callable(self.values[var]):
                    try:
                        content = content.replace("$" + var, str(self.values[var]()))
                    except TypeError:
                        raise Exception("You cant set var to function that need to get vars")
                else:
                    content = content.replace("$" + var, str(self.values[var]))

        c = ""
        for x in text:
            c += str(x)
        content = content.replace("$content", c)
        del c

        with open(self.fileName + ".txt", "a") as f:
            f.write(content)
            f.write("\n")
        if self.pr:
            print(content)