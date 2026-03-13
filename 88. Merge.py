class Solution(object):
    def merge(self, nums1, m, nums2, n):
        i = m - 1        # chỉ số cuối phần nums1 có dữ liệu
        j = n - 1        # chỉ số cuối nums2
        k = m + n - 1    # vị trí ghi từ cuối nums1

        # trộn từ cuối mảng
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1

        # nếu nums2 còn phần tử thì chép nốt
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1
