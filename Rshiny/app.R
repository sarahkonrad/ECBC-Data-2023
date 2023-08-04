#
# This is a Shiny web application. You can run the application by clicking
# the 'Run App' button above.
#
# Find out more about building applications with Shiny here:
#
#    http://shiny.rstudio.com/
#

library(shiny)
library(bslib)



  
# Define UI for application that draws a histogram
ui <- navbarPage(
  # Title of shiny app
  title = "ECBC Data+ 2023",
  theme = bs_theme(version = 4, bootswatch = "sandstone"),
  collapsible = TRUE,
  tags$head(tags$style("#test .modal-dialog {width: fit-content !important;}")),
  
    # Sidebar with a slider input for number of bins
    tabPanel("Cosine Similarity",
    sidebarLayout(
        sidebarPanel(
          selectInput("cos_sim", "Topic", 
                      choices = c("Indian", 
                                  "Irish Part 1",
                                  "Irish Part 2",
                                  "Irish Part 1 Subcorpus",
                                  "Irish Part 2 Subcorpus",
                                  "Portuguese Part 1",
                                  "Portuguese Part 2",
                                  "Powhatan",
                                  "Spanish Part 1",
                                  "Spanish Part 2",
                                  "Spanish Part 1 Subcorpus",
                                  "Spanish Part 2 Subcorpus",
                                  "Enslaved African Part 1",
                                  "Enslaved African Part 2",
                                  "Enslaved African Part 1 Subcorpus",
                                  "Enslaved African Part 2 Subcorpus",
                                  "Cannibal",
                                  "Powhatan Subcorpus",
                                  "Servant Part 1 Subcorpus",
                                  "Servant Part 2 Subcorpus",
                                  "Virginia Part 1",
                                  "Virginia Part 2",
                                  "Virginia Part 1 Subcorpus",
                                  "Virginia Part 2 Subcorpus"
                                  )),
          actionButton("run_cs", "View Cosine Similarity"),
          h4(" "),
          h4(strong("Cosine Similarity Description")),
          h6("These Cosine Similarity graphs were generated using", 
            strong("word embeddings with Word2Vec."),
            br(),
            br(),
            "Here, we can see the cosine 
            similarity", 
            strong("between a keyword and multiple different words 
            and how much that changes over time."), 
            "Cosine similarity allows 
            us to see", 
            strong("how closely related two keywords are to each other,"), 
            "and whether that relation is", strong("positive or negative."), 
            br(),
            br(),
            "Cosine similarity",strong("does not"), 
            "take into account how frequently a word appears, 
            but the context and how close in proximity two words are being used together."),
          h4(strong("Instructions:")),
          h6("Some of our subcorpora have been", 
             strong("split into multiple different graphs."), 
             br(),
             br(),
            "To access each visualization, click the drop-down menu and select which graph 
            you would like to see. These graphs are", strong("all interactive!"), 
            "If you", strong("move your 
             mouse over each line,"), 
             "you will be given the exact cosine similarity score 
             for each period. And if you go to the",
              strong("top menu bar,"),             
            "you can select the option to view multiple different cosine scores on the graph at a time.")
        ),

        # Show a plot of the generated distribution
        mainPanel(
          htmlOutput("cos_sim")
        )
    )
),

tabPanel("Word Embeddings",
         sidebarLayout(
           sidebarPanel(
             selectInput("topic_we", "Topic", 
                         choices = c("Spiritual Profit",
                                     "Powhatan", 
                                     "Virginia",
                                     "Spanish",
                                     "Enslaved African",
                                     "Irish",
                                     "Indentured"
                                     )),
             selectInput("time_we", "Time Period & Subcorpus", 
                         choices = c("1590-1594", 
                                     "1595-1599",
                                     "1600-1604",
                                     "1605-1609", 
                                     "1610-1614", 
                                     "1615-1619",
                                     "1620-1622",
                                     "1623-1626",
                                     "1627-1630",
                                     "1631-1635",
                                     "1636-1639",
                                     "Subcorpus")),
             actionButton("run_heatmap", "View Heatmap"),
             h4(" "),
             h4(strong("Heatmaps Description")),
             h6(strong("Heat maps"), 
                "are generated with", strong("word embeddings using Word2Vec."), 
                "Here, we can see multiple sets of keywords and if they are being 
                used in a similar context in our distinct sub-corpora. The", 
                strong("darker"), 
                "the shade of the square that the two keywords share, the", 
                strong("more closely"), 
                "they are associated with one another.")
             ),
           
           # Show a plot of the generated distribution
           mainPanel(
             htmlOutput("heatmap")
           )
)
),

tabPanel("Part of Speech",
         sidebarLayout(
           sidebarPanel(
             selectInput("topic_pos", "Topic", 
                         choices = c("Virginia",
                                     "Powhatan",
                                     "Indian",
                                     "Savage",
                                     "Spanish",
                                     "Negro",
                                     "Guinea",
                                     "Irish",
                                     "Servant",
                                     "Apprentice",
                                     "West Indies",
                                     "Guyana",
                                     "Cannibal",
                                     "Carib",
                                     "African"
                                     )),
             selectInput("word", "Type", 
                         choices = c("Adjectives",
                                     "Nouns", 
                                     "Verbs")),
             actionButton("run_pos", "View Part of Speech Tagging"),
             h4(" "),
             h4(strong("POS Description")),
             h6(strong("Part of Speech tagging (POS)"),
                "allows us to see the top ten", 
                strong("adjectives, nouns, and verbs"), 
                "that are closely associated with the keywords we are tracking. 
                POS gives a grammatical breakdown of the keywords we are examining, 
                and how the language surrounding them is developing to be either 
                negative or positive. ",
                br(),
                br(),
                "There are several", 
                strong("limitations"), 
                "to this method, however, in that some words are being tagged in the 
                incorrect part of speech (for example, 'Raleigh' being tagged as a verb). 
                This limitation will be further explored in future work."),
             h4(" "),
             h4(strong("Instructions:")),
             h6("To access the POS visualizations, 
                click the drop-down menu and", strong("choose which TOPIC (or keyword)"), 
                "you would like to observe, and then click the next drop-down 
                menu and choose whether you would like to see", 
                strong("adjectives, nouns, 
                or verbs associated with that topic."))
             
           ),
           
           # Show a plot of the generated distribution
           mainPanel(
             uiOutput("pos")
           )
         )
),

tabPanel("Bi-grams Over Time",
         sidebarLayout(
           sidebarPanel(
             selectInput("corpus_bigram", "Corpus", 
                         choices = c("Werowocomoco - People/Places",
                                     "Werowocomoco - Conversion",
                                     "Spanish",
                                     "Enslaved Africans",
                                     "Irish",
                                     "Indentured",
                                     "West Indies",
                                     "Bellarmine Catholic",
                                     "Bellarmine Popish",
                                     "Bellarmine Trent",
                                     "Portugal",
                                     "The Netherlands War(Attackers)",
                                     "The Netherlands War (Defenders)",
                                     "The Netherlands Subjugation",
                                     "The Netherlands Sovereignty")),
             actionButton("run_bigram", "View Bi-grams Over Time"),
             h4(" "),
             h4(strong("N-grams Description")),
             h6("Bi-grams look at unique pairings 
                with keywords and how often these 
                two words are used in conjunction 
                with one another. For our bi-gram 
                visualizations, each was generated 
                using a specific", 
                strong("sub-corpora and keywords 
                associated with the sub-corpora,"), 
                "Bi-grams are able to give us an insight into the", 
                strong("close association between two words,"), "and
                if that association is used more in a", 
                strong("certain 
                time range than others."), 
                br(),
                br(),
                "Since the sub-corpora 
                we used to generate both bi-grams and uni-grams 
                was much", 
                strong("smaller compared to other sub-corpora 
                we generated for different visualizations,"), 
                "and because bi-grams track specific word pairs, 
                some periods there are no mentions of a certain bi-gram. 
                This", 
                strong("does not"), 
                "mean that the topic that a bi-gram may be 
                referring to is not being discussed, but just that that 
                specific word combination may not have been used."),
              h4(" "),
             h4(strong("Instructions:")),
             h6("These line graphs are", strong("interactive!"), 
                "To access more information than what is just shown, ",
                strong("move your mouse over each of the lines to on the graph"),
                "to get specific frequency for each term pair. ",
                br(),
                br(),
                "The",
                strong("bar menu"),
                "at the top of the graph allows you to 
                choose whether or not to see the frequency for just one word 
                pair over time or all of the word pairs. 
                At the top, you can also", 
                strong("zoom in"), 
                "on certain areas 
                of the graph, and",
                strong("move the axis"), "as you please.")
            
             
           ),
           
           # Show a plot of the generated distribution
           mainPanel(
             uiOutput("bigram")
           )
         )
),

tabPanel("Uni-grams Over Time",
         sidebarLayout(
           sidebarPanel(
             selectInput("corpus_uni", "Corpus", 
                         choices = c("Werowocomoco",
                                     "Spanish Part 1",
                                     "Spanish Part 2",
                                     "Enslaved Africans",
                                     "Irish",
                                     "Indentured",
                                     "West Indies",
                                     "Bellarmine",
                                     "Portugal",
                                     "The Netherlands"
                                     )),
             actionButton("run_uni", "View Uni-grams Over Time"),
             h4(" "),
             h4(strong("Uni-grams Description")),
             h6("Uni-grams track the frequency of", 
                strong("single keywords"), 
                "in a focused subcorpus over time. Each unigram was 
                chosen", strong("based on its significance"), 
                "to the sub-corpus as a whole and was seen frequently discussed in texts. 
                Since the sub-corpora we used to generate both bi-grams 
                and uni-grams were", 
                strong("much smaller compared to other sub-corpora 
                we generated for different visualizations,"), 
                "in some periods there may be no mentions of a specific keyword due to a limited amount of texts."),
             h4(" "),
             h4(strong("Instructions:")),
             h6("These line graphs are", strong("interactive!"), 
                "To access more information than what is just shown, ",
                strong("move your mouse over each of the lines to on the graph"),
                "to get specific frequency for each term pair. ",
                br(),
                br(),
                "The",
                strong("bar menu"),
                "at the top of the graph allows you to 
                choose whether or not to see the frequency for just one word 
                pair over time or all of the word pairs. 
                At the top, you can also", 
                strong("zoom in"), 
                "on certain areas 
                of the graph, and",
                strong("move the axis"), "as you please."),
             
           
             
             
           ),
           
           # Show a plot of the generated distribution
           mainPanel(
             uiOutput("unigram")
           )
         )
)
)
  




# Define server logic
server <- function(input, output, session) {
  

  getcos_sim = function(){
    addResourcePath("www","www")
    if(input$cos_sim == "Indian"){
      print("get Indian cos_sim")
      src = "www/cos_sim/Indian_CSS.html"
    }
    
    if(input$cos_sim == "Irish Part 1"){
      print("get Irish1 cos_sim")
      src = "www/cos_sim/Irish1_CSS.html"
    }
    if(input$cos_sim == "Irish Part 2"){
      print("get Irish2 cos_sim")
      src = "www/cos_sim/Irish2_CSS.html"
    }
    if(input$cos_sim == "Portuguese Part 1"){
      print("get Portuguese Part 1 cos_sim")
      src = "www/cos_sim/Portuguese1_CSS.html"
    }
    if(input$cos_sim == "Portuguese Part 2"){
      print("get Portuguese Part 2 cos_sim")
      src = "www/cos_sim/Portuguese2_CSS.html"
    }
    if(input$cos_sim == "Powhatan"){
      print("get Powhatan cos_sim")
      src = "www/cos_sim/Powhatan_CSS.html"
    }
    if(input$cos_sim == "Spanish Part 1"){
      print("get Spain Part 1 cos_sim")
      src = "www/cos_sim/Spain1_CSS.html"
    }
    if(input$cos_sim == "Spanish Part 2"){
      print("get Spain Part 2 cos_sim")
      src = "www/cos_sim/Spain2_CSS.html"
    }
     # today!!
   
    if(input$cos_sim == "Enslaved African Part 1"){
      src = "www/cos_sim/African1_CSS.html"
    }
    if(input$cos_sim == "Enslaved African Part 1 Subcorpus"){
      src = "www/cos_sim/African1_subc_CSS.html"
    }
    if(input$cos_sim == "Enslaved African Part 2"){
      src = "www/cos_sim/African2_CSS.html"
    }
    if(input$cos_sim == "Enslaved African Part 2 Subcorpus"){
      src = "www/cos_sim/African2_subc_CSS.html"
    }
    if(input$cos_sim == "Cannibal"){
      src = "www/cos_sim/Cannibal_CSS.html"
    }
    if(input$cos_sim == "Powhatan Subcorpus"){
      src = "www/cos_sim/Powhatan_subc_CSS.html"
    }
    if(input$cos_sim == "Servant Part 1 Subcorpus"){
      src = "www/cos_sim/Servant1_subc_CSS.html"
    }
    if(input$cos_sim == "Servant Part 2 Subcorpus"){
      src = "www/cos_sim/Servant2_CSS.html"
    }
    if(input$cos_sim == "Virginia Part 1"){
      src = "www/cos_sim/Virginia1_CSS.html"
    }
    if(input$cos_sim == "Virginia Part 1 Subcorpus"){
      src = "www/cos_sim/Virginia1_subc_CSS.html"
    }
    if(input$cos_sim == "Virginia Part 2"){
      src = "www/cos_sim/Virginia2_CSS.html"
    }
    if(input$cos_sim == "Virginia Part 2 Subcorpus"){
      src = "www/cos_sim/Virginia2_subc_CSS.html"
    }
    if(input$cos_sim == "Irish Part 1 Subcorpus"){
      src = "www/cos_sim/Ireland1_subc_CSS.html"
    }
    if(input$cos_sim == "Irish Part 2 Subcorpus"){
      src = "www/cos_sim/Ireland2_subc_CSS.html"
    }
    if(input$cos_sim == "Spanish Part 1 Subcorpus"){
      src = "www/cos_sim/Spanish1_subc_CSS.html"
    }
    if(input$cos_sim == "Spanish Part 2 Subcorpus"){
      src = "www/cos_sim/Spanish2_subc_CSS.html"
    }
    
    
    
    print(src)
    return(src)
  }
 
  # display the html for bigram
  gethtml_bi = function(){
    if(input$corpus_bigram == "Indentured"){
      src = "www/Indentured_Bigram.html"
    }
    
    if(input$corpus_bigram == "Irish"){
      print("call ireland html for bigram")
      src = "www/Ireland_Bigram.html"
    }
    
    if(input$corpus_bigram == "Spanish"){
      src = "www/Spanish_Bigram.html"
    }
    
    if(input$corpus_bigram == "Werowocomoco - Conversion"){
      src = "www/Werowocomoco_Christian_Bigram.html"
    }
    
    if(input$corpus_bigram == "Werowocomoco - People/Places"){
      src = "www/Werowocomoco_people_place_Bigram.html"
    }
    
    if(input$corpus_bigram == "West Indies"){
      src = "www/WestIndies_Bigram.html"
    }
    
    if(input$corpus_bigram == "Enslaved Africans"){
      src = "www/EnslavedAfrica_Bigram.html"
    }
    
    if(input$corpus_bigram == "The Netherlands War(Attackers)"){
      src = "www/Netherlands_War(Attacks)_Bigram.html"
    }
    
    if(input$corpus_bigram == "The Netherlands War (Defenders)"){
      src = "www/Netherlands_War(Defenders)_Bigram.html"
    }
    
    if(input$corpus_bigram == "The Netherlands Sovereignty"){
      src = "www/Netherlands_Sovereignty_Bigram.html"
    }
    
    if(input$corpus_bigram == "The Netherlands Subjugation"){
      src = "www/Netherlands_Subjugation_Bigram.html"
    }
    
    if(input$corpus_bigram == "Portugal"){
      src = "www/Portugal_Bigram.html"
    }
    
    if(input$corpus_bigram == "Bellarmine Catholic"){
      src = "www/Bellarmine_Catholic_Bigram.html"
    }
    
    if(input$corpus_bigram == "Bellarmine Popish"){
      src = "www/Bellarmine_PopishPersecution_Bigram.html"
    }
    
    if(input$corpus_bigram == "Bellarmine Trent"){
      src = "www/Bellarmine_TrentPersecution_Bigram.html"
    }
    
    
                                     
                                     
    print(src)
    return(src)
  }
  
  # Display the html for unigram
  gethtml = function(){
    # Unigrams
    if(input$corpus_uni == "Indentured"){
      src = "www/Indentured_Unigram.html"
    }
    if(input$corpus_uni == "Irish"){
      print("get Ireland unigram")
      src = "www/Ireland_Unigram.html"
    }
    if(input$corpus_uni == "Spanish Part 1"){
      src = "www/Spanish_Unigram1.html"
    }
    if(input$corpus_uni == "Spanish Part 2"){
      src = "www/Spanish_Unigram2.html"
    }
    
    if(input$corpus_uni == "Werowocomoco"){
      src = "www/Werowocomoco_Unigram.html"
    }
    if(input$corpus_uni == "West Indies"){
      src = "www/WestIndies_Unigram.html"
    }
    if(input$corpus_uni == "Enslaved Africans"){
      src = "www/EnslavedAfrica_Unigram.html"
    }
    if(input$corpus_uni == "The Netherlands"){
      src = "www/Netherlands_Unigram.html"
    }
    if(input$corpus_uni == "Portugal"){
      src = "www/Portugal_Unigram.html"
    }
    if(input$corpus_uni == "Bellarmine"){
      src = "www/Bellarmine_Unigram.html"
    }
    
    print(src)
    
    return(src)
    
  }
  
  # display heatmap images
  getheatmap = function(){
    addResourcePath("www", "www")
    if (input$topic_we == "Enslaved African"){
      if (input$time_we == "1590-1594"){
        src = "www/heatmaps/enslaved_african/enslaved1590-94.png"
      }
      if(input$time_we == "1595-1599"){
        src = "www/heatmaps/enslaved_african/enslaved1595-99.png"
      }
      if(input$time_we == "1600-1604"){
        src = "www/heatmaps/enslaved_african/enslaved1600-04.png"
      }
      if(input$time_we == "1605-1609"){
        src = "www/heatmaps/enslaved_african/enslaved1605-09.png"
      }
      if(input$time_we == "1610-1614"){
        src = "www/heatmaps/enslaved_african/enslaved1610-14.png"
      }
      if(input$time_we == "1615-1619"){
        src = "www/heatmaps/enslaved_african/enslaved1615-19.png"
      }
      if(input$time_we == "1620-1622"){
        src = "www/heatmaps/enslaved_african/enslaved1620-22.png"
      }
      if(input$time_we == "1623-1626"){
        src = "www/heatmaps/enslaved_african/enslaved1623-26.png"
      }
      if(input$time_we == "1627-1630"){
        src = "www/heatmaps/enslaved_african/enslaved1627-30.png"
      }
      if(input$time_we == "1631-1635"){
        src = "www/heatmaps/enslaved_african/enslaved1631-35.png"
      }
      if(input$time_we == "1636-1639"){
        src = "www/heatmaps/enslaved_african/enslaved1636-39.png"
      }
      if(input$time_we == "Subcorpus"){
        src = "www/heatmaps/enslaved_african/enslavedEnslavementsubcorpus.png"
      }
    }
    
    if (input$topic_we == "Indentured"){
      if (input$time_we == "1590-1594"){
        src = "www/heatmaps/indentured/indentured1590-94.png"
      }
      if(input$time_we == "1595-1599"){
        src = "www/heatmaps/indentured/indentured1595-99.png"
      }
      if(input$time_we == "1600-1604"){
        src = "www/heatmaps/indentured/indentured1600-04.png"
      }
      if(input$time_we == "1605-1609"){
        src = "www/heatmaps/indentured/indentured1605-09.png"
      }
      if(input$time_we == "1610-1614"){
        src = "www/heatmaps/indentured/indentured1610-14.png"
      }
      if(input$time_we == "1615-1619"){
        src = "www/heatmaps/indentured/indentured1615-19.png"
      }
      if(input$time_we == "1620-1622"){
        src = "www/heatmaps/indentured/indentured1620-22.png"
      }
      if(input$time_we == "1623-1626"){
        src = "www/heatmaps/indentured/indentured1623-26.png"
      }
      if(input$time_we == "1627-1630"){
        src = "www/heatmaps/indentured/indentured1627-30.png"
      }
      if(input$time_we == "1631-1635"){
        src = "www/heatmaps/indentured/indentured1631-35.png"
      }
      if(input$time_we == "1636-1639"){
        src = "www/heatmaps/indentured/indentured1636-39.png"
      }
      if(input$time_we == "Subcorpus"){
        src = "www/heatmaps/indentured/indenturedIndenturedSubcorp.png"
      }
      
    }
    
    if (input$topic_we == "Irish"){
      if (input$time_we == "1590-1594"){
        src = "www/heatmaps/irish/irish1590-94.png"
      }
      if(input$time_we == "1595-1599"){
        src = "www/heatmaps/irish/irish1595-99.png"
      }
      if(input$time_we == "1600-1604"){
        src = "www/heatmaps/irish/irish1600-04.png"
      }
      if(input$time_we == "1605-1609"){
        src = "www/heatmaps/irish/irish1605-09.png"
      }
      if(input$time_we == "1610-1614"){
        src = "www/heatmaps/irish/irish1610-14.png"
      }
      if(input$time_we == "1615-1619"){
        src = "www/heatmaps/irish/irish1615-19.png"
      }
      if(input$time_we == "1620-1622"){
        src = "www/heatmaps/irish/irish1620-22.png"
      }
      if(input$time_we == "1623-1626"){
        src = "www/heatmaps/irish/irish1623-26.png"
      }
      if(input$time_we == "1627-1630"){
        src = "www/heatmaps/irish/irish1627-30.png"
      }
      if(input$time_we == "1631-1635"){
        src = "www/heatmaps/irish/irish1631-35.png"
      }
      if(input$time_we == "1636-1639"){
        src = "www/heatmaps/irish/irish1636-39.png"
      }
      if(input$time_we == "Subcorpus"){
        src = "www/heatmaps/irish/irishIrishSubcorp.png"
      }
      
    }
    
    if (input$topic_we == "Powhatan"){
      if (input$time_we == "1590-1594"){
        src = "www/heatmaps/powhatan/note.png"
      }
      if(input$time_we == "1595-1599"){
        src = "www/heatmaps/powhatan/note.png"
      }
      if(input$time_we == "1600-1604"){
        src = "www/heatmaps/powhatan/note.png"
      }
      if(input$time_we == "1605-1609"){
        src = "www/heatmaps/powhatan/note.png"
      }
      if(input$time_we == "1610-1614"){
        src = "www/heatmaps/powhatan/indigenous1610-14.png"
      }
      if(input$time_we == "1615-1619"){
        src = "www/heatmaps/powhatan/indigenous1615-19.png"
      }
      if(input$time_we == "1620-1622"){
        src = "www/heatmaps/powhatan/indigenous1620-22.png"
      }
      if(input$time_we == "1623-1626"){
        src = "www/heatmaps/powhatan/indigenous1623-26.png"
      }
      if(input$time_we == "1627-1630"){
        src = "www/heatmaps/powhatan/indigenous1627-30.png"
      }
      if(input$time_we == "1631-1635"){
        src = "www/heatmaps/powhatan/note.png"
      }
      if(input$time_we == "1636-1639"){
        src = "www/heatmaps/powhatan/note.png"
      }
      if(input$time_we == "Subcorpus"){
        src = "www/heatmaps/powhatan/powhatanVirginiaSubcorp.png"
      }
    }
    
    if (input$topic_we == "Spanish"){
      if (input$time_we == "1590-1594"){
        src = "www/heatmaps/spanish/spanish1590-94.png"
      }
      if(input$time_we == "1595-1599"){
        src = "www/heatmaps/spanish/spanish1595-99.png"
      }
      if(input$time_we == "1600-1604"){
        src = "www/heatmaps/spanish/spanish1600-04.png"
      }
      if(input$time_we == "1605-1609"){
        src = "www/heatmaps/spanish/spanish1605-09.png"
      }
      if(input$time_we == "1610-1614"){
        src = "www/heatmaps/spanish/spanish1610-14.png"
      }
      if(input$time_we == "1615-1619"){
        src = "www/heatmaps/spanish/spanish1615-19.png"
      }
      if(input$time_we == "1620-1622"){
        src = "www/heatmaps/spanish/spanish1620-22.png"
      }
      if(input$time_we == "1623-1626"){
        src = "www/heatmaps/spanish/spanish1623-26.png"
      }
      if(input$time_we == "1627-1630"){
        src = "www/heatmaps/spanish/spanish1627-30.png"
      }
      if(input$time_we == "1631-1635"){
        src = "www/heatmaps/spanish/spanish1631-35.png"
      }
      if(input$time_we == "1636-1639"){
        src = "www/heatmaps/spanish/spanish1636-39.png"
      }
      if(input$time_we == "Subcorpus"){
        src = "www/heatmaps/spanish/spanishSpanishSubcorp.png"
      }
    }
    
    if (input$topic_we == "Spiritual Profit"){
      if (input$time_we == "1590-1594"){
        src = "www/heatmaps/spiritual_profit/spiritual1590-94.png"
      }
      if(input$time_we == "1595-1599"){
        src = "www/heatmaps/spiritual_profit/spiritual1595-99.png"
      }
      if(input$time_we == "1600-1604"){
        src = "www/heatmaps/spiritual_profit/spiritual1600-04.png"
      }
      if(input$time_we == "1605-1609"){
        src = "www/heatmaps/spiritual_profit/spiritual1605-09.png"
      }
      if(input$time_we == "1610-1614"){
        src = "www/heatmaps/spiritual_profit/spiritual1610-14.png"
      }
      if(input$time_we == "1615-1619"){
        src = "www/heatmaps/spiritual_profit/spiritual1615-19.png"
      }
      if(input$time_we == "1620-1622"){
        src = "www/heatmaps/spiritual_profit/spiritual1620-22.png"
      }
      if(input$time_we == "1623-1626"){
        src = "www/heatmaps/spiritual_profit/spiritual1623-26.png"
      }
      if(input$time_we == "1627-1630"){
        src = "www/heatmaps/spiritual_profit/spiritual1627-30.png"
      }
      if(input$time_we == "1631-1635"){
        src = "www/heatmaps/spiritual_profit/spiritual1631-35.png"
      }
      if(input$time_we == "1636-1639"){
        src = "www/heatmaps/spiritual_profit/spiritual1636-39.png"
      }
      if(input$time_we == "Subcorpus"){
        src = "www/heatmaps/spiritual_profit/spiritualprofitVirginiaSubcorp.png"
      }
    }
    
    if (input$topic_we == "Virginia"){
      if (input$time_we == "1590-1594"){
        src = "www/heatmaps/virginia/note.png"
      }
      if(input$time_we == "1595-1599"){
        src = "www/heatmaps/virginia/virginia1595-99.png"
      }
      if(input$time_we == "1600-1604"){
        src = "www/heatmaps/virginia/virginia1600-04.png"
      }
      if(input$time_we == "1605-1609"){
        src = "www/heatmaps/virginia/virginia1605-09.png"
      }
      if(input$time_we == "1610-1614"){
        src = "www/heatmaps/virginia/virginia1610-14.png"
      }
      if(input$time_we == "1615-1619"){
        src = "www/heatmaps/virginia/virginia1615-19.png"
      }
      if(input$time_we == "1620-1622"){
        src = "www/heatmaps/virginia/virginia1620-22.png"
      }
      if(input$time_we == "1623-1626"){
        src = "www/heatmaps/virginia/virginia1623-26.png"
      }
      if(input$time_we == "1627-1630"){
        src = "www/heatmaps/virginia/virginia1627-30.png"
      }
      if(input$time_we == "1631-1635"){
        src = "www/heatmaps/virginia/virginia1631-35.png"
      }
      if(input$time_we == "1636-1639"){
        src = "www/heatmaps/virginia/virginia1636-39.png"
      }
      if(input$time_we == "Subcorpus"){
        src = "www/heatmaps/virginia/virginiaVirginiaSubcorp.png"
      }
    }
    
    return(src)
  }
  
  # display POS images 
  getpos = function(){
    if(input$topic_pos == "Negro"){
      if(input$word == "Adjectives"){
        src = "www/POSvis/Negro_adj.png"
      }
      if(input$word == "Nouns"){
        src = "www/POSvis/Negro_nouns.png"
      }
      if(input$word == "Verbs"){
        src = "www/POSvis/Negro_verbs.png"
      }
    }
    
    if(input$topic_pos == "Irish"){
      if(input$word == "Adjectives"){
        src = "www/POSvis/irish_adj.png"
      }
      if(input$word == "Nouns"){
        src = "www/POSvis/irish_nouns.png"
      }
      if(input$word == "Verbs"){
        src = "www/POSvis/irish_verbs.png"
      }
    }
    
    if(input$topic_pos == "Spanish"){
      if(input$word == "Adjectives"){
        src = "www/POSvis/Spanish_adj.png"
      }
      if(input$word == "Nouns"){
        src = "www/POSvis/Spanish_nouns.png"
      }
      if(input$word == "Verbs"){
        src = "www/POSvis/Spanish_verbs.png"
      }
    }
    
    if(input$topic_pos == "Virginia"){
      if(input$word == "Adjectives"){
        src = "www/POSvis/Virginia_adj.png"
      }
      if(input$word == "Nouns"){
        src = "www/POSvis/Virginia_nouns.png"
      }
      if(input$word == "Verbs"){
        src = "www/POSvis/Virginia_verbs.png"
      }
    }
    
    if(input$topic_pos == "Indian"){
      if(input$word == "Adjectives"){
        src = "www/POSvis/Indian_adj.png"
      }
      if(input$word == "Nouns"){
        src = "www/POSvis/Indian_nouns.png"
      }
      if(input$word == "Verbs"){
        src = "www/POSvis/Indian_verbs.png"
      }
    }
    
    if(input$topic_pos == "Powhatan"){
      if(input$word == "Adjectives"){
        src = "www/POSvis/Powhatan_adj.png"
      }
      if(input$word == "Nouns"){
        src = "www/POSvis/Powhatan_nouns.png"
      }
      if(input$word == "Verbs"){
        src = "www/POSvis/Powhatan_verbs.png"
      }
    }
    
    if(input$topic_pos == "Cannibal"){
      if(input$word == "Adjectives"){
        src = "www/POSvis/Cannibal_adj.png"
      }
      if(input$word == "Nouns"){
        src = "www/POSvis/Cannibal_nouns.png"
      }
      if(input$word == "Verbs"){
        src = "www/POSvis/Cannibal_verbs.png"
      }
    }
    
    if(input$topic_pos == "Servant"){
      if(input$word == "Adjectives"){
        src = "www/POSvis/Servant_adj.png"
      }
      if(input$word == "Nouns"){
        src = "www/POSvis/Servant_nouns.png"
      }
      if(input$word == "Verbs"){
        src = "www/POSvis/Servant_verbs.png"
      }
    }
    
    if(input$topic_pos == "West Indies"){
      if(input$word == "Adjectives"){
        src = "www/POSvis/Westindies_adj.png"
      }
      if(input$word == "Nouns"){
        src = "www/POSvis/Westindies_nouns.png"
      }
      if(input$word == "Verbs"){
        src = "www/POSvis/Westindies_verbs.png"
      }
    }
    
    if(input$topic_pos == "Apprentice"){
      if(input$word == "Adjectives"){
        src = "www/POSvis/apprentice_adj.png"
      }
      if(input$word == "Nouns"){
        src = "www/POSvis/apprentice_nouns.png"
      }
      if(input$word == "Verbs"){
        src = "www/POSvis/apprentice_verbs.png"
      }
    }
    
    if(input$topic_pos == "Carib"){
      if(input$word == "Adjectives"){
        src = "www/POSvis/carib_adj.png"
      }
      if(input$word == "Nouns"){
        src = "www/POSvis/carib_nouns.png"
      }
      if(input$word == "Verbs"){
        src = "www/POSvis/carib_verbs.png"
      }
    }
    
    if(input$topic_pos == "Guinea"){
      if(input$word == "Adjectives"){
        src = "www/POSvis/Guinea_adj.png"
      }
      if(input$word == "Nouns"){
        src = "www/POSvis/Guinea_nouns.png"
      }
      if(input$word == "Verbs"){
        src = "www/POSvis/Guinea_verbs.png"
      }
    }
    
    if(input$topic_pos == "Guyana"){
      if(input$word == "Adjectives"){
        src = "www/POSvis/guyana_adj.png"
      }
      if(input$word == "Nouns"){
        src = "www/POSvis/guyana_nouns.png"
      }
      if(input$word == "Verbs"){
        src = "www/POSvis/guyana_verbs.png"
      }
    }
    
    if(input$topic_pos == "Savage"){
      if(input$word == "Adjectives"){
        src = "www/POSvis/savage_adj.png"
      }
      if(input$word == "Nouns"){
        src = "www/POSvis/savage_nouns.png"
      }
      if(input$word == "Verbs"){
        src = "www/POSvis/savage_verbs.png"
      }
    }
    
    if(input$topic_pos == "African"){
      if(input$word == "Adjectives"){
        src = "www/POSvis/african_adj.png"
      }
      if(input$word == "Nouns"){
        src = "www/POSvis/african_nouns.png"
      }
      if(input$word == "Verbs"){
        src = "www/POSvis/african_verbs.png"
      }
    }
    
    return(src)
  }
  
  # Display cos_sim
  observeEvent(input$cos_sim, {
    output$cos_sim = renderUI({
      addResourcePath("www", "www")
      tags$iframe(
        seamless = "seamless",
        src = getcos_sim(),
        height = 600,
        width = 900)
    })
  })
  
# Display POS
  observeEvent(input$run_pos, {
    output$pos = renderUI({
      addResourcePath("www", "www")
      src_list <- getpos()
      img_tags <- lapply(src_list, function(src) {
        tags$img(src = src, height = "100%", width = "100%")
      })
      do.call(tags$div, img_tags)
    })
  })
  

  # Display Bi-grams based on selections
  observeEvent(input$run_bigram, {
    output$bigram = renderUI({
      addResourcePath("www", "www")
      tags$iframe(
        seamless = "seamless",
        src = gethtml_bi(),
        height = 500,
        width = 850)
    })
  })
  
  
  # Display Uni-grams based on selections
  observeEvent(input$run_uni, {
    output$unigram = renderUI({
      addResourcePath("www", "www")
      tags$iframe(
        seamless = "seamless",
        src = gethtml(),
        height = 500,
        width = 850)
    })
    
  })
 
  
  
# Show Heatmap in the modal dialog
  observeEvent(input$run_heatmap, {
    output$heatmap = renderUI({
      addResourcePath("www", "www")
      src_list <- getheatmap()
      img_tags <- lapply(src_list, function(src) {
        tags$img(src = src, height = "80%", width = "80%")
      })
      do.call(tags$div, img_tags)
    })
  })
  
  
}

# Run the application 
shinyApp(ui = ui, server = server)
