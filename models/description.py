class Description:
    def __init__(self, description):
        self.description = description

    def create_description(self):
        # Set the maximum description characters
        description = ''
        line_max = 4
        char_max = 32
        for b in range(0, len(self.description), char_max):
            subs = self.description[b:b + char_max] + '\n'
            description = description + subs
            line_max = line_max - 1
            if line_max == 0:
                break
        return description
