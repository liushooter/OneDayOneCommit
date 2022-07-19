for file in *.ts; do
  [ -f "$file" ] || continue
  filname=${file%%.*}

  echo "$filname"
  key=00000000000000000000000000000000
  iv=0000000000000000
  tsfile=$file
  out="./$filname.mp4"
  echo "$out"

  openssl enc -d -aes-128-cbc -iv $iv -K $key -in $tsfile -out $out
done