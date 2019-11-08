from mrjob.job import MRJob


class netflix_count(MRJob):
    def mapper(self, _, line):
        for word in line.split():
            if word.findall() == "stock":
                yield "stock", 1

    def reducer(self, key, values):
        yield key, sum(values)


if __name__ == "__main__":
    netflix_count.run()
