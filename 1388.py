LEETCODE 1388. Pizza With 3n Slices 解题思路分析

public int maxSizeSlices(int[] slices) {
    // 记忆数组
    int[][] memo=new int[slices.length][slices.length/3+1];
    // 从第1位到倒数第2位范围内选择的最大的结果
    int res1= help(slices,0,slices.length-2,0,memo);
    memo=new int[slices.length][slices.length/3+1];
    // 从第2位到倒数第1位范围内选择的最大的结果
    int res2= help(slices,1,slices.length-1,0,memo);
    // 两者最大值为返回结果
    return Math.max(res1, res2);
}
int help(int[] slices,int start,int end,int count, int[][] memo){
    // 如果已经选择完所有披萨，返回0
    if(count==slices.length/3) return 0;
    // 如果剩余披萨中不够选择，返回-1
    if(slices.length/3-count>(end-start+2)/2) return -1;
    if(memo[start][count]>0)return memo[start][count];
    int max=0;
    for(int i=start;i<=end;i++){
        int sum=help(slices,i+2,end,count+1,memo);
        if(sum==-1) break;
        max=Math.max(max,slices[i]+sum);
    }
    memo[start][count]=max;
    return max;
}

 
← LEETCODE 1392. Longest Happy Prefix 解题思路分析LEETCODE 1387. Sort Integers by The Power Value 解题思路分析 →
LEETCODE 1388. Pizza With 3n Slices 解题思路分析
发表于2020年3月24日由kwantong
题目大意：

3n 块披萨

给你一个披萨，它由 3n 块不同大小的部分组成，现在你和你的朋友们需要按照如下规则来分披萨：

你挑选 任意 一块披萨。
Alice 将会挑选你所选择的披萨逆时针方向的下一块披萨。
Bob 将会挑选你所选择的披萨顺时针方向的下一块披萨。
重复上述过程直到没有披萨剩下。
每一块披萨的大小按顺时针方向由循环数组 slices 表示。

请你返回你可以获得的披萨大小总和的最大值。

示例 1：


输入：slices = [1,2,3,4,5,6]
输出：10
解释：选择大小为 4 的披萨，Alice 和 Bob 分别挑选大小为 3 和 5 的披萨。然后你选择大小为 6 的披萨，Alice 和 Bob 分别挑选大小为 2 和 1 的披萨。你获得的披萨总大小为 4 + 6 = 10 。
示例 2：


输入：slices = [8,9,8,6,1,1]
输出：16
解释：两轮都选大小为 8 的披萨。如果你选择大小为 9 的披萨，你的朋友们就会选择大小为 8 的披萨，这种情况下你的总和不是最大的。
示例 3：

输入：slices = [4,1,2,5,8,3,1,9,7]
输出：21
示例 4：

输入：slices = [3,1,2]
输出：3
提示：

1 <= slices.length <= 500
slices.length % 3 == 0
1 <= slices[i] <= 1000
如果想查看本题目是哪家公司的面试题，请参考以下免费链接： https://leetcode.jp/problemdetail.php?id=1388

解题思路分析：

本题的题意很明确，当自己选完一块披萨之后，另外两个人会拿走与之相邻的两片，因此我们可以得到一个很重要的结论，即无论如何，你也不可能拿到相邻的两片披萨。换句话说，如果我们拿到的所有披萨都不相邻，则一定是一个合理的情况。因此本题目就转化为，在一个长度为3n的数组中找到n个不相邻并且和最大数字。另外注意一点，由于披萨是圆形，因此，数组中首元素与尾元素同样属于相邻元素。

由于要保证首尾两个数字不能同时选择，因此我们可以从数组的第1到3n-1位范围内选取不相邻并且和最大的n个数，再从第2位到第3n位选取，两者最大值即是返回结果。

解题时，我们可以考虑使用递归加记忆数组的思路。递归函数需要三个重要参数，数组起始下标，数组结束下标，以及当前已选择的个数。当已选择个数等于n时结束递归。递归函数中，我们从起始下标循环至结束下标，循环中任意当前数字都是可选择的对象，选择一个数字后，我们递归到子问题继续求解，递归时，由于不能选择与当前相邻的元素，因此起始下标变为当前下标加2，结束下标不变，已选择个数加一。当前数值加上子问题递归结果为当前结果，循环后取得最大结果作为本层递归的返回值。
