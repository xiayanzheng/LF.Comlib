class Core:

    def gen_range(self, StartNumber, EndNumber, GapNumber):
        number_range_result = []
        row_number_sp = StartNumber
        gap = int(EndNumber) - int(StartNumber)
        if gap > GapNumber:
            for X in range(int(gap / GapNumber)):
                temp = []
                temp.append(row_number_sp)
                temp.append(row_number_sp + GapNumber)
                number_range_result.append(temp)
                row_number_sp += GapNumber
            temp = []
            temp.append(row_number_sp)
            temp.append(row_number_sp + int(gap % GapNumber))
            number_range_result.append(temp)
            row_number_sp += int(gap % GapNumber)
        else:
            number_range_result.append([StartNumber, EndNumber])
        return number_range_result

    def byte_to_gb(self, data, round_num=0):
        if type(data) is int:
            return round(int(data) / 1024 / 1024 / 1024, round_num)
        else:
            raise TypeError
