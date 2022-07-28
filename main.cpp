// void decryptAndPrint(void)

// {
//   int uVar1;
//   int local_25;
//   int local_21;
//   int local_1d;
//   int local_19;
//   int local_15;
//   int local_11;
//   int local_10;
  
//   puts("Maybe you are in the right path ??");
//   local_25 = 0x6474ea66;
//   local_21 = 0x5770b365;
//   local_1d = 0x3b72f707;
//   local_19 = 0x6625e127;
//   local_15 = 0x4f37cd12;
//   local_11 = 0;
//   for (local_10 = 0; local_10 < 0x14; local_10 = local_10 + 1) {
//     uVar1 = (int)(local_10 >> 0x1f) >> 0x1e;
//     *(byte *)((int)&local_25 + local_10) =
//          *(byte *)((int)&local_25 + local_10) ^ (&stack0x00000000)[(local_10 + uVar1 & 3) - uVar1];
//   }
//   printf("\nFlag you got is : %s",(char *)&local_25);
//                     /* WARNING: Subroutine does not return */
// }


// void getInput(void)

// {
//   char local_2a [38];
  
//   puts("Enter:");
//   __isoc99_scanf(&DAT_0804a00f,local_2a);
//   printf("Value entered: %s\n",local_2a);
//   return;
// }

#include <stdio.h>
#include <iostream>
#include <bits/stdc++.h>
using namespace std;
int main(int param_1)

{
    int local_25=0x6474ea66;
    int f=0x26;
    for(int i=0;i<20;i++){

        std::cout<<(uint)((i>>0x1f)>>0x1a);
            *(char *)((int)&local_25 + i) =
         *(char *)((int)&local_25 + i) ^ (&f)[i];

    }
      printf("\nFlag you got is : %s",(char *)&local_25);

//   getInput();
//   putchar(10);
//                     /* WARNING: Subroutine does not return */
//   exit(0);
return 0;
}


eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjp7ImlkIjoiNWY0NzkwOWI4OTljNzYwMDM0YTEyMTQ2IiwiZW1haWwiOiJjczUxOTA0MjFAY3NlLmlpdGQuYWMuaW4iLCJmaXJzdG5hbWUiOiJBbmlydWRoYSIsImxhc3RuYW1lIjoiS3Vsa2FybmkiLCJ1c2VybmFtZSI6ImNzNTE5MDQyMSIsInJvbGVzIjpbImlpdGRfdXNlciIsImdvb2dsZXIiLCJsZHpzVFhRayIsInlMcW5lUEdtIiwiOFcwVmN4bWIiLCJ3SU5Zc3VUeSIsIkR4R2M5M3dyIl0sInByaXZpbGVnZSI6MSwiaXN2ZXJpZmllZCI6dHJ1ZX0sImlhdCI6MTY0OTc2MTY2MywiZXhwIjoxNjU0OTQ1NjYzLCJpc3MiOiJhdXRoLmRldmNsdWIuaW4ifQ.fQHvOi22GBxl5r_NL2QWy9NEDbh0PcFAIye7yxN4XxZ71TC87CI7Xnjjm46WayidtiUpgHsc6jrt_Gbpe4Dr0uAAmTKHmrL0FOZYqT7x6UejEyhD7dM1mg8pxcSToJZUrWbXPz6QfSLvrrwSLtHcdmpFNC5yghVP6tngzMJM24fBugKbxZm63d20plVQQMkeDYEKwXeDuPS3kVMUIyP-CEZ1JtDEEh9xPmM5vo3b514KJ4ZTQAHMJXQ2fzG8vcSmVLAuOu_7HE6Ardgx8kTOg-4haU2ZOFuaOz-zK9uAPX203g0fWY-duXqyF_BqX99EPzaqXv24VkIIf0w1nXftJg