#include <iostream>
#include <vector>

using namespace std;


int productOfAll(vector<int> lst){
  int product = 1;
  for(vector<int>::iterator it = lst.begin(); it != lst.end(); ++it){
    product = *it * product;
  }
  return product;
}

vector<int> productOfAllButi(vector<int> lst){
  int product = productOfAll(lst);
  vector<int> productList = lst;
  int newProduct;
  for(int i = 0; i < productList.size(); i++){
    newProduct = product / productList[i];
    productList[i] = newProduct;
  }
  return productList;
}




int main()
{
    vector<int> lst;
    lst.push_back (1);
    lst.push_back (2);
    lst.push_back (3);
    lst.push_back (4);
    lst.push_back (5);
    vector<int> answer = productOfAllButi(lst);
    for(int i = 0; i < answer.size(); i++){
      cout << " " << answer[i];
    }

    return 0;
}
