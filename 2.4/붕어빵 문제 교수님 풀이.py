#!/usr/bin/env python
# coding: utf-8

# In[ ]:


진기의 붕어빵


# In[ ]:


T = int(input())
for tc in range(1,T+1):
    '''
    N : 손님수
    M : 붕어빵 만드는 시간
    K : 갯수
    '''

    N, M, K = map(int, input().split())
    customer = list(map(int, input().split()))
    
    remain = 0          # 붕어빵 재고
    ans = 'Possible'    # 가능여부
    
    for i in range(11112):
            if i % M == 0 and i != 0:
                remain += K
            for c in customer:
                if c == i:
                    if remain ==0:
                        ans = 'Impossible'
                        break
                remain -= 1
    
    print('#{} {}'.format(tc, ans))
            

