from model import GPT2PPL

# initialize the model
model = GPT2PPL()

sentence = "Artemy Vedel (1767–1808) was a Ukrainian-born Russian composer of military and liturgical music. He made major contributions to the music of Ukraine, producing works based on Ukrainian folk melodies, and is one of the greatest composers of Ukrainian and Russian classical music of his era. Born in Kyiv, he studied at the Kyiv-Mohyla Academy, after which he was appointed its conductor. The army general Andrei Levanidov acquired his services to lead Kyiv's regimental chapel and choir, where he reached the peak of his creativity as a composer. He was then based in Kharkiv but returned to Kyiv when cultural life was affected by Tsar Paul I's decrees. He became a novice monk of the Kyiv Pechersk Lavra, but was accused of threatening the royal family and incarcerated as a mental patient. His work was censored while Ukraine was part of the Soviet Union. More than 80 of his works are known, including 31 choral concertos, but many of his compositions are lost."

model(sentence)