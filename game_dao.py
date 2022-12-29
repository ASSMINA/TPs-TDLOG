from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:////tmp/tdlog.db', echo=True, future=True)
Base = declarative_base(bind=engine)
Session = sessionmaker(bind=engine)

class GameEntity(Base):
 __tablename__ = 'game'
 id = Column(Integer, primary_key=True)
 players = relationship("PlayerEntity", back_populates="game",
 cascade="all, delete-orphan")

class PlayerEntity(Base):
 __tablename__ = 'player'
 id = Column(Integer, primary_key=True)
 name = Column(String, nullable=False)
 game_id = Column(Integer, ForeignKey("game.id"), nullable=False)
 game = relationship("GameEntity", back_populates="players")
 battle_field = relationship("BattlefieldEntity",
 back_populates="player",
 uselist=False, cascade="all, delete-orphan")

class BattlefieldEntity(Base):
 __tablename__='battlefield'
 id= Column(Integer,primary_key=True)
 min_x= Column(Integer)
 min_y= Column(Integer)
 min_z= Column(Integer)
 max_x= Column(Integer)
 max_y= Column(Integer)
 max_z= Column(Integer)
 max_power= Column(Integer)
 player_id= Column(Integer,ForeignKey("player.id"), nullable=False)
 player= relationship( "PlayerEntity",back_populate="battlefield")
 vessel= relationship ( "VesselEntity", back_populate="battlefield",  cascade="all, delete-orphan")


class VesselEntity(Base):
 __tablename__='vessel'
 id= Column(Integer, primary_key=True, nullable=False)
 coord_x= Column(Integer)
 coord_y= Column(Integer)
 coord_z= Column(Integer)
 hits_to_be_destroyed= Column(Integer)
 type= Columb(string)
 battle_field_id= Column(Integer,ForeignKey("battle_field.id"), nullable=False)
 battlefield = relationship("BattlefieldEntity", back_populate="vessel")
 weapon= relationship("WeaponEntity", back_populate="vessel", cascade="all, delete-orphan")

def VesselEntity.type:
CRUISER = "Cruiser"
DESTROYER = "Destroyer"
FRIGATE = "Frigate"
SUBMARINE = "Submarine"


class WeaponEntity(Base):
 __tablename__='Weapon'
 id= Columb(Integer, primary_key=True, nullable=False)
 ammunitions= Column(Integer)
 rangee= Column(Integer)
 type= Column(string)
 vessel_id= Column(Integer,ForeignKey("vessel.id"), nullable=False)
 vessel = relationship("VesselEntity", back_populate="weapon")


def WeaponEntity.type:
AIRMISSILELAUNCHER = "AirMissileLauncher"
SURFACEMISSILELAUNCHER = "SurfaceMissileLauncher"
TORPEDOLAUNCHER = "TorpedoLauncher"


class GameDao:
 def __init__(self):
   Base.metadata.create_all()
   self.db_session = Session()

 def map_to_game(game_entity):
    game().type= Game

 def create_game(self, game: Game) -> int:
   game_entity = map_to_game_entity(game)
   self.db_session.add(game_entity)
   self.db_session.commit()
   return game_entity.id

 def map_to_game (game):
   game_entity().type= GameEntity

 def find_game(self, game_id: int) -> Game:
   stmt = select(GameEntity).where(GameEntity.id == game_id)
   game_entity = self.db_session.scalars(stmt).one()
   return map_to_game(game_entity)

 def create_PlayerEntity(self, PlayerEntity: PlayerEntity) -> int:
  player_entity = map_to_player_entity(player)
  self.db_session.add(player_entity)
  self.db_session.commit()
  return player_entity.id

 def find_PlayerEntity(self, PlayerEntity_id: int) -> player:
   stmt = select(PlayerEntity).where(PlayerEntity.id == player_id)
   player_entity = self.db_session.scalars(stmt).one()
   return map_to_player(player_entity)

 def create_VesselEntity(self, VesselEntity: VesselEntity) -> int:
  vessel_entity = map_to_vessel_entity(vessel)
  self.db_session.add(vessel_entity)
  self.db_session.commit()
  return vessel_entity.id

 def find_VesselEntity(self, VesselEntity_id: int) -> vessel:
   stmt = select(VesselEntity).where(VesselEntity.id == vessel_id)
   vessel_entity = self.db_session.scalars(stmt).one()
   return map_to_vessel(vessel_entity)