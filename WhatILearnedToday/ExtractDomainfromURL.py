l1 = [3,7,5,11,32]
l2 = [12,15,16,18,10]
x = []
count = 0
dict_l1 = {}
target  = 18

for x,y in enumerate(l1):
    diff = target - y
    if diff in dict_l1:
        return [x, target[diff]]
    else:
        dict_l1[x] = y

           

        # while count < str_range:
        #     for k,v in word_dict.items():
        #         if word_dict[k] 
            
            # if word_dict[i] in word_dict:
            #     answer_list.append(word_dict[i])



#     def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
#         result = []
#         if head == None:
#             return head
#         current = head

#         while current != None:
#             var1 = current.next
#             current.next = Node(current.val, var1, None)
#             current = var1
#             current = head
#         while current != None:
#             if current.random != None:
#                 current.next.random = current.random.next
#                 current = current.next.next
#                 current = head
#                 copyHead = head.next
#         while current != None:
#             var1 = current.next.next
#             copy = current.next
#             current.next = var1
#                 if tmp != None:
#                 copy.next = var1.next
#             current =template
#         return copyHead

#         for i in head:
#             new_node = Node(head,i[0],i[1])
#             result.append(new_node)
#             print(result)
            
#         # while len(result) <= len(head):
# Solution.copyRandomList(head)
# xz = [[1,2],[2,4],[4,8]]

# def something(x: list):
#     for i in xz:
#         print(i)


# something(xz)