#include<iostream>
#include<vector>
using namespace std;
void onoff(int* vec, int _idx);

void onoff(int* vec, int _idx)
{
   if (vec[_idx] == 1)
   {
      vec[_idx] = 0;
   }
   else
   {
      vec[_idx] = 1;
   }
}

void Man(int *_arr, int num, int Light_size)
{
   for (int i = num; i <= Light_size; i += num)
   {
      onoff(_arr, i);
   }
}

void Woman(int *_arr, int num, int Light_size)
{
   int idx = 1;
   while (true)
   {
      if (num - idx < 1 || num + idx > Light_size || _arr[num-idx] != _arr[num+idx])
      {
         break;
      }
      if (_arr[num - idx] == _arr[num + idx])
      {
         onoff(_arr, num - idx);
         onoff(_arr, num + idx);
      }
      idx++;   
   }
   onoff(_arr, num);
}


int main()
{

   cin.tie(0);
   ios::sync_with_stdio;
   int Light_size, T, Light;
   int Gender, num;
   cin >> Light_size;
   int arr[101];
   for (int i = 1; i <= Light_size; i++)
   {
      cin >> arr[i];
   }
   cin >> T;
   for (int i = 0; i < T; i++)
   {
      cin >> Gender >> num;

      if (Gender == 1)
      {
         Man(arr, num, Light_size);

      }

      else if (Gender == 2)
      {
         Woman(arr, num, Light_size);
      }
   }
   for (int i = 1; i <= Light_size; i++)
   {
      cout << arr[i] << " ";
      if (i % 20 == 0)
      {
         cout << "\n";
      }
   }
}
