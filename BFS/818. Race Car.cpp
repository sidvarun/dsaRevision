
class Solution {
    public int racecar(int target) {
        Set<String> visited = new HashSet<>(); 
        Queue<StateNode> queue = new LinkedList<>();
        queue.add(new StateNode(1, 0));
        int distance = 0;
        while (!queue.isEmpty()) {
            int levelSize = queue.size();
            for (int i = 0; i < levelSize; i++) {
                StateNode cur = queue.poll();
                if (cur.position == target) {
                    return distance;
                }
                // if A
                int nextPosition = cur.position + cur.speed;
                int nextSpeed = cur.speed * 2;
                if (!visited.contains(nextSpeed + "," + nextPosition)) {
                    visited.add(nextSpeed + "," + nextPosition);
                    queue.offer(new StateNode(nextSpeed, nextPosition));
                }             
                // if R
                nextPosition = cur.position;
                nextSpeed = cur.speed > 0 ? -1 : 1;
                if (!visited.contains(nextSpeed + "," + nextPosition)) {
                    visited.add(nextSpeed + "," + nextPosition);
                    queue.offer(new StateNode(nextSpeed, nextPosition));
                }
            }
            distance++;
        }
        return -1;
    }

    class StateNode {
        int speed;
        int position;

        public StateNode(int speed, int position) {
            this.speed = speed;
            this.position = position;
        }
    }
}

/*********************************************************************************************/

class Solution {
public:
    int racecar(int target) {
        // 1. Initialize double ended queue as 0 moves, 0 position, +1 velocity
        queue<vector<int>> q;
        q.push({0, 0, 1});
        while (!q.empty()) {
            
            vector<int> item = q.front();
            q.pop();
            
            // (moves) moves, (pos) position, (vel) velocity)
            int moves = item[0];
            int pos = item[1];
            int vel = item[2];
            
            if (pos == target) return moves;
            
            // Avoid integer overflow - stop whenever we've passed twice the magnitude of target.
            if (abs(pos) > 2 * target) continue;
            
            // 2. Always consider moving the car in the direction it is already going
            q.push({moves + 1, pos + vel, 2 * vel});
            
            // 3. Only consider changing the direction of the car if one of the following conditions is true
            //    i.  The car is driving away from the target.
            //    ii. The car will pass the target in the next move.  
            if ((pos + vel > target && vel > 0) || (pos + vel < target && vel < 0)) {
                q.push({moves + 1, pos, (vel > 0) ? -1 : 1});
            }
        }
        
        return 0;
    }
};