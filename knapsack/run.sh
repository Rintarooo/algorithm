#!/bin/bash
#$ sudo chmod 744 run.sh

for arg in "$@"; do 
	 if [ "${arg##*.}" = "py" ]; then
	 	# if file is ***.py 
	 	PY=${arg}
	 	echo "execute file:". ${PY}
	 else
	 	echo "input file:". ${arg}
	 	echo "output:"
	 	python ${PY} < ${arg}
	 	echo ""
	 fi
done