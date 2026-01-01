class Solution:
  def reverseKGroup(self, head, k):
    count, n = 0, head
    while n and count < k:
      n = n.next
      count += 1
    if count < k: return head
    new_head, prev = self.reverse(head, count)
    head.next = self.reverseKGroup(new_head, k)
    return prev
    
  def reverse(self, head, count, prev = None):
      while count > 0:
        nxt = head.next
        head.next = prev
        prev = head
        head = nxt
        count -= 1
      return (head, prev)