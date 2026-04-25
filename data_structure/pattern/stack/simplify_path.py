# LC 71 - Simplify Path (Problem Challenge)
#
# PROBLEM: Given Unix absolute path string, simplify it.
#   "."  → current directory (ignore)
#   ".." → go up one directory (pop from stack)
#   ""   → double slash (ignore)
#   else → valid directory name (push)
#
# PATTERN: Stack - directory navigation
#   Stack represents the current path from root.
#   ".." → pop (go back one level)
#   valid name → push (go deeper)
#   join with "/" at end
#
# ANALOGY: Browser back button 🌐
#   Each folder you enter → push to history
#   ".." → click back → pop last visited
#   "."  → refresh → stay same → ignore

def simplify_path(path):
    stack = []
    parts = path.split('/')   # split on "/"

    for part in parts:
        if part == '' or part == '.':
            continue          # ignore empty and current dir
        elif part == '..':
            if len(stack) > 0:
                stack.pop()   # go up one level
        else:
            stack.append(part)  # valid dir → go deeper

    return '/' + '/'.join(stack)


print(simplify_path("/home/"))                    # "/home"
print(simplify_path("/../"))                      # "/"
print(simplify_path("/home//foo/"))               # "/home/foo"
print(simplify_path("/a/./b/../../c/"))           # "/c"
print(simplify_path("/a/../../b/../c//.//"))      # "/c"
