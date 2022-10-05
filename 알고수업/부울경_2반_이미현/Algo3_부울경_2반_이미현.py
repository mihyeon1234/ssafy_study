'''
1) 가중치의 최소 비용으로 만들어진 신장 트리로 모든 간선을 연결하여야 한다.
 삼각형(사이클)이 되는 부분없어야 한다.
 간선의 갯수는 n-1(정점 - 1 ) 이다.


 2) 가중치 순으로 연결 노드를 정렬을 하고,
    삼각형(사이클)이 되지 않게 유니온과 파인드 함수를 만든후 써서
    부모를 찾은 후 같은 부모를 갖고 있지 않으면 연결해준다.
    n-1개의 간선이 선택되면 모든 간선의 가중치를 더해준다.

'''