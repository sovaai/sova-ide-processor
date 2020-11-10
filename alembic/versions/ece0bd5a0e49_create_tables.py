"""Create tables

Revision ID: ece0bd5a0e49
Revises: 
Create Date: 2020-10-18 13:02:42.425857

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'ece0bd5a0e49'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('complects_revisions',
    sa.Column('revision_id', postgresql.UUID(), server_default=sa.text('uuid_generate_v4()'), nullable=False),
    sa.Column('complect_id', postgresql.UUID(), nullable=False),
    sa.Column('revision_number', sa.Integer(), nullable=False),
    sa.Column('code', sa.String(), nullable=False),
    sa.Column('source_archive_path', sa.String(), nullable=False),
    sa.Column('binary_path', sa.String(), nullable=True),
    sa.Column('meta', postgresql.JSONB(astext_type=sa.Text()), server_default='{}', nullable=False),
    sa.Column('created', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.PrimaryKeyConstraint('revision_id'),
    sa.UniqueConstraint('code')
    )
    op.create_table('complects_revisions_seq',
    sa.Column('id', sa.BigInteger(), autoincrement=True, nullable=False),
    sa.Column('complect_id', postgresql.UUID(), nullable=False),
    sa.Column('last_revision_number', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('complect_id')
    )
    op.create_table('tasks',
    sa.Column('task_id', postgresql.UUID(), server_default=sa.text('uuid_generate_v4()'), nullable=False),
    sa.Column('status', postgresql.ENUM('enqueued', 'working', 'finished', 'failed', name='status'), nullable=False),
    sa.Column('script', sa.String(), nullable=False),
    sa.Column('type', sa.String(), nullable=False),
    sa.Column('locked_by', sa.String(), nullable=True),
    sa.Column('args', postgresql.JSONB(astext_type=sa.Text()), nullable=True),
    sa.Column('result', postgresql.JSONB(astext_type=sa.Text()), nullable=True),
    sa.Column('errortext', sa.String(), nullable=True),
    sa.Column('meta', postgresql.JSONB(astext_type=sa.Text()), server_default='{}', nullable=False),
    sa.Column('extra', postgresql.JSONB(astext_type=sa.Text()), nullable=True),
    sa.Column('created', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.Column('updated', sa.DateTime(timezone=True), nullable=True),
    sa.PrimaryKeyConstraint('task_id')
    )
    op.create_table('task_reports',
    sa.Column('id', sa.BigInteger(), autoincrement=True, nullable=False),
    sa.Column('task_id', postgresql.UUID(), nullable=False),
    sa.Column('status', postgresql.ENUM('enqueued', 'working', 'finished', 'failed', name='status'), nullable=False),
    sa.Column('meta', postgresql.JSONB(astext_type=sa.Text()), server_default='{}', nullable=False),
    sa.Column('created', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.ForeignKeyConstraint(['task_id'], ['tasks.task_id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('task_reports')
    op.drop_table('tasks')
    op.drop_table('complects_revisions_seq')
    op.drop_table('complects_revisions')
    # ### end Alembic commands ###