sudo ps -ef | grep node | awk '{print $2}' | xargs kill -9


find ./ -type f -name "*.less" | xargs  rename "s/less/scss/"

find ./ -type f -name "*.po"  | xargs  -I {} cp {} <new_path> #复制
