class Solution:
    def fullJustify(self, words, maxWidth):
        res = []
        i = 0
        n = len(words)

        while i < n:
            # B1: lấy các từ cho 1 dòng
            line_len = len(words[i])
            j = i + 1

            while j < n and line_len + 1 + len(words[j]) <= maxWidth:
                line_len += 1 + len(words[j])
                j += 1

            line_words = words[i:j]
            num_words = j - i

            # B2: tạo dòng
            if j == n or num_words == 1:
                # dòng cuối hoặc 1 từ → căn trái
                line = " ".join(line_words)
                line += " " * (maxWidth - len(line))
            else:
                # chia đều khoảng trắng
                total_chars = sum(len(w) for w in line_words)
                total_spaces = maxWidth - total_chars
                gaps = num_words - 1

                space = total_spaces // gaps
                extra = total_spaces % gaps

                line = ""
                for k in range(gaps):
                    line += line_words[k]
                    line += " " * (space + (1 if k < extra else 0))
                line += line_words[-1]

            res.append(line)
            i = j

        return res