class Solution(object):
    def get_path_content(self, identifier):
        splits = identifier.split(' ')
        root = splits[0]
        files = splits[1:]
        paths = []
        contents = []
        
        for file in files:
            contents.append(file.split('(')[1].split(')')[0])
            paths.append(root + '/' + file.split('(')[0])
        return paths, contents
        
    def findDuplicate(self, paths):
        """
        :type paths: List[str]
        :rtype: List[List[str]]
        """
        res = {}
        for path in paths:
            paths, contents = self.get_path_content(path)
            for i in range(len(contents)):
                if contents[i] in res:
                    res[contents[i]].append(paths[i])
                else:
                    res[contents[i]] = []
                    res[contents[i]].append(paths[i])
        new_res = []
        for k, v in res.items():
            if len(v) > 1:
                new_res.append(v)
        return new_res
        
