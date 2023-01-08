while IFS="" read -r p || [ -n "$p" ]
do
  printf '%s\n' "$p"
  curl 'http://dev.team.thm/script.php?page='"$p"
done < paths.txt
