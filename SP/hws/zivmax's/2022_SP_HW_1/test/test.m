prime = [2 3];
judge = 0;
for i = 2:100
 for j = 2:fix(sqrt(i))
 if mod(i,j) == 0
 judge = 0;
 break;
 else 
 judge = 1;
 end
 end
 if judge == 1
 prime = [prime,i];
 end
end
disp(prime)
