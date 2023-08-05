# 2023.5.3,  loading 230537 essays 
import requests,time, fire,json, spacy, fileinput ,traceback
from __init__ import * 
nlp = spacy.load('en_core_web_sm')

def run(infile, idxname:str=None, debug:bool=False, postag:bool=False, reset:bool=True):
	''' essays-dis.jsonl.gz, 2023.5.2 '''
	if idxname is None : idxname = infile.split('.')[0] 
	if reset: drop(idxname)
	check(idxname) 
	start = time.time()
	for i, line in enumerate(fileinput.input(infile,openhook=fileinput.hook_compressed)): 
		try:
			arr = json.loads(line.strip()) # dis
			info, dsk, spa = arr['info'], arr.get('dsk',''), arr['spacy'] 
			did = f"doc-{i}"
			print (f"[index-dis] {infile}:\t", did, flush=True) 

			info.update({'type': 'doc' ,'did': did})
			esindex(idxname, did, info ) # add essay 
			if dsk: dskindex(idxname, did, dsk) # add dsk 

			tdoc = spacy.tokens.Doc(nlp.vocab).from_json( spa )
			for j, sp in enumerate( tdoc.sents):
				doc = sp.as_doc() 
				sntid = f"{did}:snt-{j}"
				source = skenp(doc)
				source.update({"did":did, "sntid":sntid, "type":"snt", "tc": len(sp),"snt":sp.text.strip()}) 
				esindex(idxname, sntid, source ) 

				[esindex(idxname, f"{sntid}:tok-{t.i}", {"did": did, 'sntid': sntid, 'i': t.i, 'type':'tok', 'rid': info.get('rid',0), 'uid': info.get('uid',0),'lex': t.text, 'lem':t.lemma_, 'pos':t.pos_, 'tag':t.tag_, 'dep':t.dep_, 'govlem': t.head.lemma_, 'govpos': t.head.pos_ }) for t in doc]

		except Exception as e:
			print("ex:", e)	
			exc_type, exc_value, exc_traceback_obj = sys.exc_info()
			traceback.print_tb(exc_traceback_obj)

	print(f"indexing finished: {idxname}, \t| using: ", time.time() - start) 

if __name__ == '__main__': 	#run('testdoc', debug=True)
	fire.Fire(run)