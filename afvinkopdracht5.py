t_dna = {'A':'U', 'T':'A', 'G':'C', 'C':'G'}

class DNA:
    def __init__(self, name, seq):
        self.setName(name)
        self.setDNA(seq)

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def setDNA(self, seq):
        seq = seq.upper()

        for char in seq:
            if char not in 'ATCGN':
                return None
        self.seq = seq

    def getDNA(self):
        return self.seq

    def getTranscript(self):
        t_seq = ''
        
        for char in self.seq:
            t_seq += t_dna[char]
        return t_seq

    def getLength(self):
        return len(self.seq)

    def getGC(self):
        nuc = {'G':0,'C':0}
        
        for char in self.seq:
            if char in nuc:
                nuc[char] += 1
        
        return float((nuc['G'] + nuc['C'])/self.getLength()*100)
############################################
    def sort(self):
        if self.l_obj == []:
            self.l_obj.append()
############################################
class Sequentie:
    def __init__(self):
        self.l_obj = []
        self.main()

    def main(self):
        seqs = self.read_file('Felis_catus.Felis_catus_8.0.cdna.all.fasta')
        l_obj = self.create_objects(seqs)
        best_obj = self.check_obj(l_obj)

        print('-'*50,
              '\n' + 'The sequence with the highest GC% of', str(float(best_obj.getGC())) + '%',
              '\n' + str(best_obj.getName()),
              '\n' + str(best_obj.getDNA()),
              '\n' + str(best_obj.getTranscript()),
              '\n' + 'Length:', str(best_obj.getLength()))

    def read_file(self, file_name):
        file = open(file_name, 'r').readlines()
        seqs = []
        seq = []

        for line in file:
            line = line.rstrip()
            if '>' in line:
                if seq != []:
                    seqs.append([header, ''.join(seq)])
                    seq = []
                header = line
            else:
                seq.append(line)

        return seqs

    def create_objects(self, seqs):
        l_obj = []

        for seq in seqs:
            t_obj = DNA(seq[0], seq[1])
            l_obj.append(t_obj)

        return l_obj

    def check_obj(self, l_obj):
        high_GC = 0

        for obj in l_obj:
            if obj.getGC() > high_GC:
                best_obj = obj

        return best_obj










