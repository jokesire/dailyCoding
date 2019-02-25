#include <iostream>
#include <vector>

using namespace std;


bool sumExists(vector<int> lst, int k){
  int d;
  vector<int> seen (k , 0);
  for(vector<int>::iterator it = lst.begin(); it != lst.end(); ++it){
    d = k - *it;
    if(d < k){
      if(seen[d] == 1){
        return true;
      }
      else{
        seen[d] = 1
      }
    }
  }
  return false;
}


int main()
{
    vector<int> lst;
    lst.push_back (10);
    lst.push_back (15);
    lst.push_back (3);
    lst.push_back (7);
    bool answer = sumExists(lst , 17);
    cout << answer;

    return 0;
}
