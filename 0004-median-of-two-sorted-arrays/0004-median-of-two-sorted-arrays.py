# class Solution:
#     def findMedianSortedArrays(self, nums1, nums2):
#         if len(nums1) > len(nums2):
#             nums1, nums2 = nums2, nums1
#         m, n = len(nums1), len(nums2)
#         total = m + n
#         half = (total + 1) // 2
#         l, r = 0, m
#         while l <= r:
#             i = (l + r) // 2
#             j = half - i
#             A_left  = nums1[i-1] if i > 0 else float('-inf')
#             A_right = nums1[i]   if i < m else float('inf')
#             B_left  = nums2[j-1] if j > 0 else float('-inf')
#             B_right = nums2[j]   if j < n else float('inf')
#             if A_left <= B_right and B_left <= A_right:
#                 if total % 2:
#                     return max(A_left, B_left)
#                 return (max(A_left, B_left) + min(A_right, B_right)) / 2
#             elif A_left > B_right:
#                 r = i - 1
#             else:
#                 l = i + 1

import math
from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        
        #Je commence tout d'abord par me rassurer que nums1 est le tableau le plus court pour optimiser la recherche binaire.
        #Et si m > n, on échange les tableaux.
        if m > n:
            nums1, nums2, m, n = nums2, nums1, n, m
            
        low = 0
        high = m
        # La taille totale requise pour la moitié gauche des éléments (incluant le milieu pour le cas impair).
        half_len = (m + n + 1) // 2 
        
        while low <= high:
            # je prend P1 : le nombre d'éléments de nums1 dans la partie gauche [0, P1)
            P1 = (low + high) // 2
            
            # je definrir comme P2, le Nombre d'éléments de nums2 dans la partie gauche [0, P2)
            #ainsi que  half_len qui sera la taille totale souhaitée pour la moitié gauche.
            P2 = half_len - P1
            
            #Je définir les quatre éléments de ma frontaliers et j'Utilise -infinity et +infinity pour gérer mes cas limites
            
            # L1 (Gauche de nums1)
            L1 = nums1[P1 - 1] if P1 > 0 else float('-inf')
            
            # R1 (Droite de nums1)
            R1 = nums1[P1] if P1 < m else float('+inf')
            
            # L2 (Gauche de nums2)
            L2 = nums2[P2 - 1] if P2 > 0 else float('-inf')
            
            # R2 (Droite de nums2)
            R2 = nums2[P2] if P2 < n else float('+inf')
            
            
            if L1 <= R2 and L2 <= R1:
                #Mon Cas 1 : mon Nombre impair total (la médiane est le max de la partie gauche)
                if (m + n) % 2 == 1:
                    return float(max(L1, L2))
                
                # Mon Cas 2 : Mon Nombre pair total (la médiane est la moyenne des deux éléments du milieu)
                else:
                    return (max(L1, L2) + min(R1, R2)) / 2.0
            
            elif L1 > R2:
                # L1 est trop grand. La coupure P1 est trop à droite.
                # Déplacer la coupure P1 vers la gauche.
                high = P1 - 1
            
            else:
                #si non (L2 > R1),
                #Je cherche à déplacer la coupure P1 vers la droite.
                low = P1 + 1
        
        return 0.0