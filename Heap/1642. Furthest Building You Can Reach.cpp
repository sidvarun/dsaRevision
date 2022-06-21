// idea is to use a in heap 
// use as many ladders as possible for buildings with larger differences in height
// for the remainig climbs use bricks

int furthestBuilding(vector<int>& A, int bricks, int ladders) {
    priority_queue<int> pq;
    for (int i = 0; i < A.size() - 1; i++) {
        int d = A[i + 1] - A[i];
        if (d > 0)
            pq.push(-d);
        if (pq.size() > ladders) {
            bricks += pq.top();
            pq.pop();
        }
        if (bricks < 0)
            return i;
    }
    return A.size() - 1;
}

