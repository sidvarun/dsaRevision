class Solution {
public:
    
    //Custom function for sorting in incraesing order of lastDay
    static bool cmp(vector<int> a,vector<int> b)
    {
        return a[1]<b[1];
    }
    
    int scheduleCourse(vector<vector<int>>& courses) {
        
        //Sorting in increasing order of lastDay
        sort(courses.begin(),courses.end(),cmp);
        
        //This Priority Queue Will be used to store duration of course we will op for
        //If the Deadline of a course cant be met we will remove the largest duration course 
        //and add lesser duartion course
        priority_queue<int> pq;  //MaxHeap
        
        int totalDays=0;
        int n=courses.size();
        for(int i=0;i<n;i++)
        {
            int dur=courses[i][0];  //Duration
            int deadline=courses[i][1];  //LastDay
            
            if(totalDays+dur<=deadline)
            {
                totalDays+=dur;
                pq.push(dur);
            }
            else if(!pq.empty() && pq.top()>dur)  //pq is not empty
            {
                    totalDays+=(dur-pq.top());
                    pq.pop();
                    pq.push(dur);
            }
        }
        return pq.size();
    }
};