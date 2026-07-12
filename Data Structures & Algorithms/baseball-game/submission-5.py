class Solution:
    def calPoints(self, operations: List[str]) -> int:
        count = 0
        records = []
        for index, op in enumerate(operations):
            if op == '+':
                length = len(records)
                num = int(records[length-1]) + int(records[length - 2])
                count += num
                records.append(num)
            elif op == 'D':
                print("records", records, index)
                num = 2*(int(records[len(records)-1]))
                count += num
                records.append(num)
            elif op == 'C':                
                num = records.pop()
                count -= num                
            else:
                count += int(op)
                records.append(int(op))
        print(records)
        return count
        