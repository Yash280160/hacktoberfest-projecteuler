class Main {
  public static void main(String[] args) {
   int i,a,b=1;
   for (a=3;b<10001;a++)
   {
   for (i=2;a>i;i++)
   { if (a%i==0)
      break;
   }
   if (a==i)
   b++;
   }
   System.out.print("10001th prime number is:"+(a-1));
  }
}