import discord
from discord.ext import commands
from discord import app_commands

def start():
    bot = commands.Bot(command_prefix = "£", description = "Compteur de flop !", intents = discord.Intents.all())


    @bot.event
    async def on_ready():
        print('Logged in as')
        print(bot.user.name)
        print(bot.user.id)
        print('------')
        print("Je suis là !")
        try:
            synced = await bot.tree.sync()
            print(f"Synced {len(synced)} command(s)")
        except Exception as e:
            print(e)



    ##
    @bot.tree.command(name = "flop", description = "Rajoute un flop à une personnne !")
    async def flop(ctx: discord.Interaction, txt: str):
        dic = dicflop(ctx)
        server = ctx.guild
        id = server.id

        affichage = discord.Embed(title = "Flop", color = 0x20EED8)

        listm = []
        for i in range(len(server.members)):
            listm.append("<@"+str(server.members[i].id)+">")


        if txt in listm and txt in dic:
            with open(str(id)+".txt", 'w') as f:
                for pers in dic:
                    if pers != txt:

                        f.write(pers+";"+str(int(dic[pers]))+"\n")
                    else:
                        f.write(pers+";"+str(int(dic[pers])+1)+"\n")
                        affichage.add_field(name = "", value = txt + " a flop, il a maintenant " + str(int(dic[txt])+1) +" flops !")


        else:
             affichage.add_field(name = "", value = "Cette personne n'est pas dans la liste. (/addfloppeur)")


        await ctx.response.send_message(embed = affichage, ephemeral = True)
        print(dir(ctx.guild))



    @bot.tree.command(name = "addfloppeur", description = "Rajoute un floppeur à la liste !")
    async def addfloppeur(ctx: discord.Interaction, txt: str):
        dic = dicflop(ctx)
        server = ctx.guild
        id = server.id

        affichage = discord.Embed(title = "Nouveau floppeur", color = 0xEE1CFF)

        listm = []
        for i in range(len(server.members)):
            listm.append("<@"+str(server.members[i].id)+">")


        if txt in listm and txt not in dic:
            with open(str(id)+".txt", 'a') as f:
                f.write(txt+";0\n")
                affichage.add_field(name = "", value = txt +" a bien été ajouté à la liste")
        else:
            affichage.add_field(name = "", value = "Erreur dans l'ajout")
        await ctx.response.send_message(embed = affichage)



    @bot.tree.command(name = "topflop", description = "Affiche les plus gros floppeurs !")
    async def topflop(ctx):

        dic = dicflop(ctx)
        server = ctx.guild
        id = server.id

        #Tri par nb de flop
        select = []
        while len(dic) != len(select):
            best = -1
            bestselect = None
            for pers in dic:
                if int(dic[pers]) > best and pers not in select:
                    bestselect = pers
                    best = int(dic[pers])
            select.append(bestselect)


        affichage = discord.Embed(title = "Classement du flop", description = "Voici les plus gros floppeurs :", color = 0xE13B24)
        affichage.set_thumbnail(url = "https://feedastic.com/wp-content/uploads/2021/01/Quels-sont-les-differents-moyens-dobtenir-les-coordonnees-du-prospect-1.png" )

        txtflop = ""
        for i in range(min(5, len(select))):
            if i == 0:
                txtflop+= "🥇 "
            elif i == 1:
                txtflop += "🥈 "
            elif i == 2:
                txtflop += "🥉 "
            else:
                txtflop += "✨ "

            txtflop += "**" + select[i] + "** : " + dic[select[i]]+"\n"

        affichage.add_field(name = "",value = txtflop)
        affichage.set_footer(text = "Tika sera toujours le plus gros floppeur dans nos coeurs")


        await ctx.response.send_message(embed = affichage)



    @bot.tree.command(name = "nbflop", description = "Affiche le nombre de flop d'une personne'")
    async def nbflop(ctx,txt : str):
        dic = dicflop(ctx)
        affichage = discord.Embed(title = "Nouveau floppeur", color = 0xC9FF00)

        try:
            affichage.add_field(name = "",value = txt + " est à " + str(dic[txt]) +" flop(s).")
        except:
            affichage.add_field(name = "",value ="Cette personne n'est pas dans la liste. (/addfloppeur)")

        await ctx.response.send_message(embed = affichage)


    @bot.tree.command(name = "setflop", description = "Initialise le nombre de flop d'une personne'")
    async def setflop(ctx,txt:str, nb:int):

        dic = dicflop(ctx)
        server = ctx.guild
        id = server.id

        affichage = discord.Embed(title = "Initialisation du flop", color = 0xD7DCAE)

        listm = []
        for i in range(len(server.members)):
            listm.append("<@"+str(server.members[i].id)+">")


        if txt in listm and txt in dic:
            with open(str(id)+".txt", 'w') as f:
                for pers in dic:
                    if pers != txt:

                        f.write(pers+";"+str(int(dic[pers]))+"\n")
                    else:
                        f.write(pers+";"+str(nb)+"\n")
                        affichage.add_field(name = "", value ="Cette personne a maintenant "+str(nb)+ " flops !")
        else:
            affichage.add_field(name = "",value ="Cette personne n'est pas dans la liste. (/addfloppeur)")

        await ctx.response.send_message(embed = affichage)


    ##Start le bot
    bot.run('token')

##Recupere le dico
def dicflop(ctx):
    dic = {}
    server = ctx.guild
    id = server.id
    try:
        with open(str(id)+".txt","r") as f:
            for line in f:
                data = line.split(";")
                dic[data[0]] = data[1].strip()
    except:
        with open(str(id)+".txt","w") as f:
        #pour creer le fichier s'il n'existe pas
            1+1
    return dic

start()