const longestCommonPrefix = (strs) => {
  const zip = (...strs) =>
    [...strs[0]].map((_, idx) => strs.map((str) => str[idx]));

  if (!strs.length) return "";
  const zipArray = zip(...strs);
  let prefix = "";
  for (let i = 0; i < zipArray.length; i++) {
    const setObj = new Set(zipArray[i]);
    const isSame = setObj.size === 1;
    if (isSame) {
      prefix += zipArray[i][0];
    } else {
      return prefix;
    }
  }
  return prefix;
};

const strs = ["flower", "flow", "flight"];
console.log(longestCommonPrefix(strs));
