import React, { Component } from "react";
import Card from '@material-ui/core/Card';
import CardActionArea from '@material-ui/core/CardActionArea';
import CardContent from '@material-ui/core/CardContent';
import CardMedia from '@material-ui/core/CardMedia';
import Typography from '@material-ui/core/Typography';
import { Grid } from "@material-ui/core";
import { withStyles } from '@material-ui/core/styles';
import { green, pink } from '@material-ui/core/colors';
import Instagram from '@material-ui/icons/Instagram';
import FilterListIcon from '@material-ui/icons/FilterList';
import Button from '@material-ui/core/Button'
import WhatsApp from '@material-ui/icons/WhatsApp';
import Checkbox from "@material-ui/core/Checkbox";
import Dialog from '@material-ui/core/Dialog';
import DialogTitle from '@material-ui/core/DialogTitle';
import List from '@material-ui/core/List';
import ListItem from '@material-ui/core/ListItem';
import ListItemIcon from '@material-ui/core/ListItemIcon';
import ListItemText from '@material-ui/core/ListItemText';

const useStyles = theme => ({
  root: {
    flexGrow: 1,
  },
  menuButton: {
    marginRight: theme.spacing(2),
  },
  title: {
    flexGrow: 1,
  },
  card: {
    maxWidth: 350
  },
  header: {
      padding: '0 0 8px 0 !important',
      backgroundColor: 'rgba(255, 255, 255, 0.6)'
  },
  header_card: {
      backgroundColor: 'rgba(255, 255, 255, 0.05)'
  },
  header_child: {
      padding:'0px',
      margin:'0px'
  },
  filter_container: {
    marginTop:'8px',
    marginBottom:'8px'
  },
  categories_button: {
    justifyContent:'center',
    display:'flex'
  }
});

class HomePage extends Component {

  state = {
    searchNodes: "",
    listBolo: [],
    listCategory: [],
    checked: [],
    dialogOpen: false
  };

  constructor(props) {
    debugger;
    super(props);

    this.loadQuitute()
    this.loadCategory()
    
  }

  handleToggle(value) {
    const currentIndex = this.state.checked.indexOf(value);
    let newChecked = [...this.state.checked];
    
    if(value.id == -1) {
      if (currentIndex === -1) {
        newChecked = this.state.listCategory
      } else {
        newChecked = []
      }
    }
    else if (currentIndex === -1) {
      newChecked.push(value);
    } else {
      newChecked.splice(currentIndex, 1);
    }

    if(newChecked.length > 1 || (newChecked.length == 1 && newChecked[0].id != -1)) {
      this.loadQuitute(newChecked.map((item) => item.id).join())
    } else {
      newChecked = []
      this.loadQuitute()
    }

    this.setState({
      checked: newChecked
    });

    this.setState({
      dialogOpen: false
    });
  };

  async loadQuitute(category = ""){
    var uri = '/listQuitute?category='
    if(category){
      uri = uri + category
    }
    fetch(uri)
    .then((response) =>
          response.json()
    ).then((data) => {
      this.setState({
        listBolo: data.map(
          (item) => ( {
            title:item.titulo,
            description:item.descricao,
            image:item.foto
          } )
        )
      })
    });
  }
  
  async loadCategory() {
    fetch('/listCategoria')
    .then((response) =>
          response.json()
    ).then((data) => {
      this.setState({
        listCategory: [
          {
            id:-1,
            description:"Todos",
          } 
        ].concat(
          data.map(
            (item) => ( {
              id:item.id,
              description:item.nomeCategoria,
            } )
          )
        )
      })
      
    }); 
  }
           
  
  showAlert = (description) => {
    alert(description);
  }

  

  goToAnotherUrl = (url) => {
    window.open(url, '_blank').focus();
  }

  goToWhatsApp = () => {
    this.goToAnotherUrl("https://api.whatsapp.com/send?phone=5511985935897&text=Estou%20contatando%20pelo%20site%20para%20saber%20mais%20sobre...");
  }

  goToInstagram = () => {
    this.goToAnotherUrl("https://www.instagram.com/confeitariadocesonho2106/");
  }

  dialogOpen = () => {
    this.setState({
      dialogOpen: true
    });
  }

  dialogHandleClose = () => {
    this.setState({
      dialogOpen: false
    });

  } 

    render() {
      const { classes } = this.props;
      let InstagramColorButton = withStyles((theme) => ({
        root: {
          color: '#FFFFFF',
          backgroundColor: '#E4405F',
          '&:hover': {
            backgroundColor: pink[300],
          },
        },
      }))(Button);
      
    let WhatsAppColorButton = withStyles((theme) => ({
        root: {
          color: '#FFFFFF',
          backgroundColor: '#25D366',
          '&:hover': {
            backgroundColor: green[300],
          },
        },
      }))(Button);

     return (
        <div >
        <Grid container className={classes.root}  spacing={2} justify="center">
            <Grid item xs={12} className={classes.header}>
                <Grid 
                container 
                direction="row"
                alignItems="center" 
                spacing={0}
                >
                    <Grid item ms={6} className={classes.header_child}>
                        <Card square={true} elevation={0} className={classes.header_card}>  
                            <CardMedia
                            component="img"
                            alt=""
                            image="../static/images/logo.png"
                            title=""
                            className={classes.header_card}
                            />
                        </Card>
                    </Grid>
                    <Grid item ms={6} className={classes.header_child}  >
                        <Card square={true} elevation={0} className={classes.header_card} >  
                            <CardContent className={classes.header_card}>
                                <Typography gutterBottom variant="h2" component="h2">
                                Confeitaria Doce Sonho
                                </Typography>
                                <Typography gutterBottom variant="h5" color="textSecondary" component="h2">
                                Trabalhamos com chocolate e muito amor em todas as épocas do ano!
                                </Typography>
                                <Grid
                                container
                                direction="row"
                                justifyContent="flex-start"
                                alignItems="center"
                                spacing={2}>
                                    <Grid item>
                                    <InstagramColorButton
                                        variant="outlined"
                                        color="primary"
                                        startIcon={<Instagram />}
                                        onClick={() => this.goToInstagram()}
                                    >
                                        Instagram
                                    </InstagramColorButton>
                                    </Grid>
                                    <Grid item>
                                    </Grid>
                                    <Grid item>
                                    <WhatsAppColorButton
                                        variant="outlined"
                                        color="primary"
                                        startIcon={<WhatsApp />}
                                        onClick={() => this.goToWhatsApp()}
                                    >
                                        WhatsApp
                                    </WhatsAppColorButton>
                                    </Grid>
                                </Grid>
                            </CardContent>
                            
                        </Card>
                    </Grid>
                </Grid>
            </Grid>
            <Grid item xs={10} className={classes.filter_container}>
              <Button variant="contained" color="primary" startIcon={<FilterListIcon />} onClick={() => this.dialogOpen()}>
                Filtrar
              </Button>
              <Dialog onClose={() => this.dialogHandleClose()} aria-labelledby="simple-dialog-title" open={this.state.dialogOpen}>
                <DialogTitle id="simple-dialog-title">Filtros</DialogTitle>
                <List>
                { this.state.listCategory.map((item) => (
                  <ListItem key={item} role={undefined} dense button onClick={() => this.handleToggle(item)}>
                    <ListItemIcon>
                      <Checkbox
                        edge="start"
                        tabIndex={-1}
                        checked={this.state.checked.indexOf(item) !== -1}
                        disableRipple
                        inputProps={{ 'aria-labelledby': `checkbox-list-label-${item.id}` }}
                      />
                      {/*  */}
                    </ListItemIcon>
                    <ListItemText id={item.id} primary={item.description} />
                  </ListItem>
                ))}
                </List>
              </Dialog>
            </Grid>
            <Grid item xs={10}>
                <Grid container justify="center" spacing={2}>
                { this.state.listBolo.map((item) => (
                    <Grid item>
                        <Card className={classes.card}>
                            <CardActionArea onClick={() => showAlert(item.title) }>
                                <CardMedia
                                component="img"
                                alt={item.description}
                                height="300"
                                image={"../static/" + item.image}
                                title={item.title}
                                />
                                <CardContent>
                                    <Typography gutterBottom variant="h5" component="h2">
                                        {item.title}
                                    </Typography>
                                    <Typography variant="body2" color="textSecondary" component="p">
                                        {item.description}
                                    </Typography>
                                </CardContent>
                            </CardActionArea>
                        </Card>
                    </Grid>
                ))}
                </Grid>
            </Grid>
        </Grid>
        </div>
     );
    }
  
}

export default withStyles(useStyles, { withTheme: true })(HomePage);