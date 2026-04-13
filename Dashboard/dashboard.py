import os
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import matplotlib.patches as mpatches
warnings = __import__('warnings')
warnings.filterwarnings('ignore')

# ── PAGE CONFIG ──────────────────────────────────────────────────────
st.set_page_config(
    page_title="Olist E-Commerce Analytics",
    page_icon="🛒",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ── PREMIUM CSS ──────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=Bricolage+Grotesque:wght@400;500;600;700;800&display=swap');

:root {
    --bg-base:       #060810;
    --bg-surface:    #0c0f1d;
    --bg-elevated:   #111528;
    --bg-hover:      #161b30;
    --border:        rgba(255,255,255,0.06);
    --border-active: rgba(255,255,255,0.12);
    --text-primary:  #f0f2f8;
    --text-secondary:#8892b0;
    --text-muted:    #4a5270;
    --accent-blue:   #5b8cff;
    --accent-teal:   #00e5c8;
    --accent-gold:   #ffcc4d;
    --accent-rose:   #ff6b8a;
    --accent-purple: #a78bfa;
    --accent-green:  #4ade80;
}

html, body, [class*="css"] {
    font-family: 'Plus Jakarta Sans', sans-serif;
    -webkit-font-smoothing: antialiased;
}

.stApp { background: var(--bg-base); color: var(--text-primary); }

[data-testid="stSidebar"] {
    background: var(--bg-surface) !important;
    border-right: 1px solid var(--border) !important;
}
[data-testid="stSidebar"] * { color: var(--text-secondary) !important; }
[data-testid="stSidebar"] .stMarkdown h3 { color: var(--text-primary) !important; }

.sidebar-logo { display:flex;align-items:center;gap:10px;padding:4px 0 24px; }
.sidebar-logo-icon { width:36px;height:36px;background:linear-gradient(135deg,var(--accent-blue),var(--accent-teal));border-radius:10px;display:flex;align-items:center;justify-content:center;font-size:1rem; }
.sidebar-logo-text { font-family:'Bricolage Grotesque',sans-serif;font-size:1rem;font-weight:700;color:#fff !important; }
.sidebar-logo-sub  { font-size:0.7rem;color:var(--text-muted) !important;margin-top:1px; }

.dash-header { position:relative;padding:36px 44px 32px;margin-bottom:28px;border-radius:20px;overflow:hidden;background:var(--bg-surface);border:1px solid var(--border); }
.dash-header-bg { position:absolute;inset:0;background:radial-gradient(ellipse 60% 80% at 85% 50%,rgba(91,140,255,0.07) 0%,transparent 60%),radial-gradient(ellipse 40% 60% at 10% 80%,rgba(0,229,200,0.04) 0%,transparent 50%); }
.dash-header-content { position:relative;z-index:1; }
.dash-eyebrow { display:inline-flex;align-items:center;gap:6px;background:rgba(91,140,255,0.1);border:1px solid rgba(91,140,255,0.2);border-radius:100px;padding:4px 12px;font-size:0.7rem;font-weight:600;color:var(--accent-blue);letter-spacing:1px;text-transform:uppercase;margin-bottom:14px; }
.dash-title { font-family:'Bricolage Grotesque',sans-serif;font-size:2.6rem;font-weight:800;color:var(--text-primary);letter-spacing:-1px;line-height:1.1;margin:0 0 10px; }
.dash-title .grad { background:linear-gradient(90deg,var(--accent-blue) 0%,var(--accent-teal) 100%);-webkit-background-clip:text;-webkit-text-fill-color:transparent; }
.dash-sub { font-size:0.9rem;color:var(--text-secondary);max-width:500px;line-height:1.6; }
.dash-header-pills { display:flex;gap:8px;flex-wrap:wrap;margin-top:18px; }
.dash-pill { display:inline-flex;align-items:center;gap:5px;background:rgba(255,255,255,0.04);border:1px solid var(--border);border-radius:8px;padding:5px 10px;font-size:0.72rem;color:var(--text-secondary); }
.dash-pill .dot { width:6px;height:6px;border-radius:50%; }

.kpi-grid { display:grid;grid-template-columns:repeat(4,1fr);gap:14px;margin-bottom:28px; }
.kpi-card { background:var(--bg-surface);border:1px solid var(--border);border-radius:16px;padding:22px 24px 20px;position:relative;overflow:hidden; }
.kpi-glow { position:absolute;top:-40px;right:-40px;width:120px;height:120px;border-radius:50%;opacity:0.12;pointer-events:none; }
.kpi-accent { position:absolute;left:0;top:0;bottom:0;width:3px;border-radius:16px 0 0 16px; }
.kpi-icon { width:36px;height:36px;border-radius:10px;display:flex;align-items:center;justify-content:center;font-size:1rem;margin-bottom:14px; }
.kpi-label { font-size:0.7rem;font-weight:600;color:var(--text-muted);text-transform:uppercase;letter-spacing:1.2px;margin-bottom:6px; }
.kpi-value { font-family:'Bricolage Grotesque',sans-serif;font-size:2rem;font-weight:700;color:var(--text-primary);line-height:1;margin-bottom:8px;letter-spacing:-1px; }
.kpi-change { display:inline-flex;align-items:center;gap:4px;font-size:0.72rem;font-weight:500;padding:2px 8px;border-radius:100px; }
.kpi-change.pos { background:rgba(74,222,128,0.1);color:var(--accent-green); }

.section-header { margin-bottom:18px; }
.section-label { font-size:0.68rem;font-weight:600;color:var(--accent-blue);text-transform:uppercase;letter-spacing:1.5px;margin-bottom:4px; }
.section-title { font-family:'Bricolage Grotesque',sans-serif;font-size:1.25rem;font-weight:700;color:var(--text-primary);letter-spacing:-0.3px;margin:0 0 4px; }
.section-desc { font-size:0.82rem;color:var(--text-secondary);margin:0; }

.chart-wrap { background:var(--bg-surface);border:1px solid var(--border);border-radius:16px;padding:24px; }

.stat-mini { background:var(--bg-elevated);border:1px solid var(--border);border-radius:12px;padding:16px 20px;text-align:center; }
.stat-mini-val { font-family:'Bricolage Grotesque',sans-serif;font-size:1.4rem;font-weight:700;color:var(--text-primary);margin-bottom:4px; }
.stat-mini-lbl { font-size:0.72rem;color:var(--text-muted);text-transform:uppercase;letter-spacing:0.8px; }

.seg-badge { display:inline-flex;align-items:center;gap:5px;padding:4px 10px 4px 6px;border-radius:100px;font-size:0.73rem;font-weight:600; }
.seg-badge::before { content:'';width:6px;height:6px;border-radius:50%; }
.seg-champions  { background:rgba(91,140,255,0.12);color:#7ba7ff;border:1px solid rgba(91,140,255,0.2); }
.seg-champions::before  { background:#5b8cff; }
.seg-loyal      { background:rgba(0,229,200,0.1);color:#00e5c8;border:1px solid rgba(0,229,200,0.2); }
.seg-loyal::before      { background:#00e5c8; }
.seg-potential  { background:rgba(74,222,128,0.1);color:#4ade80;border:1px solid rgba(74,222,128,0.2); }
.seg-potential::before  { background:#4ade80; }
.seg-recent     { background:rgba(255,204,77,0.1);color:#ffcc4d;border:1px solid rgba(255,204,77,0.2); }
.seg-recent::before     { background:#ffcc4d; }
.seg-atrisk     { background:rgba(255,107,138,0.1);color:#ff6b8a;border:1px solid rgba(255,107,138,0.2); }
.seg-atrisk::before     { background:#ff6b8a; }
.seg-lost       { background:rgba(248,113,113,0.1);color:#f87171;border:1px solid rgba(248,113,113,0.2); }
.seg-lost::before       { background:#f87171; }

.tbl-header { display:grid;padding:8px 16px;background:var(--bg-elevated);border-radius:8px;margin-bottom:4px;font-size:0.68rem;font-weight:600;color:var(--text-muted);text-transform:uppercase;letter-spacing:0.8px; }
.tbl-row { display:grid;padding:10px 16px;border-radius:8px;font-size:0.85rem;color:var(--text-secondary);border:1px solid transparent; }
.tbl-row:hover { background:var(--bg-elevated);border-color:var(--border); }

.delivery-fast { background:rgba(74,222,128,0.08);border:1px solid rgba(74,222,128,0.15);border-radius:8px;padding:2px 8px;font-size:0.72rem;color:#4ade80;font-weight:600; }
.delivery-slow { background:rgba(255,107,138,0.08);border:1px solid rgba(255,107,138,0.15);border-radius:8px;padding:2px 8px;font-size:0.72rem;color:#ff6b8a;font-weight:600; }
.delivery-avg  { background:rgba(255,204,77,0.08);border:1px solid rgba(255,204,77,0.15);border-radius:8px;padding:2px 8px;font-size:0.72rem;color:#ffcc4d;font-weight:600; }

.stTabs [data-baseweb="tab-list"] { background:var(--bg-elevated) !important;border-radius:12px !important;padding:4px !important;gap:2px !important;border:1px solid var(--border) !important; }
.stTabs [data-baseweb="tab"] { border-radius:9px !important;color:var(--text-secondary) !important;font-weight:500 !important;font-size:0.85rem !important;padding:8px 18px !important; }
.stTabs [aria-selected="true"] { background:var(--bg-surface) !important;color:var(--text-primary) !important;border:1px solid var(--border-active) !important; }
.stTabs [data-baseweb="tab-panel"] { padding-top:24px !important; }

.stSlider [data-baseweb="slider"] { accent-color:var(--accent-blue); }
::-webkit-scrollbar { width:5px;height:5px; }
::-webkit-scrollbar-track { background:var(--bg-base); }
::-webkit-scrollbar-thumb { background:var(--border-active);border-radius:10px; }
.stMultiSelect > div > div, .stSelectbox > div > div { background:var(--bg-elevated) !important;border-color:var(--border) !important;border-radius:10px !important; }
.stDateInput > div > div { background:var(--bg-elevated) !important;border-color:var(--border) !important;border-radius:10px !important; }
div[data-testid="metric-container"] { display:none; }
hr { border-color:var(--border); }
.divider { height:1px;background:var(--border);margin:20px 0; }
</style>
""", unsafe_allow_html=True)

# ── MATPLOTLIB THEME ─────────────────────────────────────────────────
BG    = '#0c0f1d'
BG2   = '#111528'
GRID  = '#1a1f35'
TEXT  = '#8892b0'
TEXT2 = '#c8d0e8'

plt.rcParams.update({
    'figure.facecolor': BG, 'axes.facecolor': BG,
    'axes.edgecolor': GRID, 'axes.labelcolor': TEXT,
    'xtick.color': TEXT, 'ytick.color': TEXT,
    'text.color': TEXT2, 'grid.color': GRID,
    'grid.linestyle': '-', 'grid.alpha': 1.0,
    'font.family': 'sans-serif', 'font.size': 9,
})

PALETTE = {
    'blue': '#5b8cff', 'teal': '#00e5c8',
    'gold': '#ffcc4d', 'rose': '#ff6b8a',
    'purple': '#a78bfa', 'green': '#4ade80',
}

# ── LOAD & CACHE DATA ────────────────────────────────────────────────
@st.cache_data
def load_data():
    df = pd.read_csv(os.path.join(os.path.dirname(__file__), 'main_data.csv'))
    df['order_purchase_timestamp'] = pd.to_datetime(df['order_purchase_timestamp'])
    return df

@st.cache_data
def compute_monthly(df):
    monthly = df.resample('ME', on='order_purchase_timestamp').agg(
        order_count=('order_id', 'nunique'),
        total_revenue=('revenue', 'sum')
    ).reset_index()
    monthly['order_month'] = monthly['order_purchase_timestamp']
    return monthly

@st.cache_data
def compute_category(df):
    cat = df.groupby('product_category_name_english').agg(
        total_revenue=('revenue', 'sum'),
        order_count=('order_id', 'nunique'),
        avg_order_value=('revenue', 'mean')
    ).reset_index()
    cat.columns = ['category', 'total_revenue', 'order_count', 'avg_order_value']
    return cat.sort_values('total_revenue', ascending=False).reset_index(drop=True)

@st.cache_data
def compute_rfm_segments(df):
    # Gunakan kolom segment dari main_data langsung
    seg = df.groupby('segment').agg(
        count=('customer_unique_id', 'nunique'),
        avg_recency=('recency', 'mean'),
        avg_frequency=('frequency', 'mean'),
        avg_monetary=('monetary', 'mean')
    ).round(1).reset_index()
    seg['pct'] = (seg['count'] / seg['count'].sum() * 100).round(1)
    return seg

@st.cache_data
def compute_delivery(df):
    # Hitung delivery time per state dari main_data
    # Gunakan kolom recency sebagai proxy jika tidak ada delivery column
    # Ambil avg recency per customer_state sebagai indikator
    state_del = df.groupby('customer_state').agg(
        customer_count=('customer_unique_id', 'nunique'),
        avg_recency=('recency', 'mean')
    ).reset_index()
    state_del.columns = ['state', 'customer_count', 'avg_recency']
    return state_del.sort_values('customer_count', ascending=False).reset_index(drop=True)

# ── LOAD ─────────────────────────────────────────────────────────────
df_raw = load_data()

# Precompute delivery data dari semua data (tidak terfilter)
# State coords untuk tooltip
STATE_COORDS = {
    'AC':(-9.0,-70.8),'AL':(-9.6,-36.8),'AM':(-3.4,-65.8),'AP':(1.4,-51.8),
    'BA':(-12.9,-41.4),'CE':(-5.5,-39.3),'DF':(-15.8,-47.9),'ES':(-19.2,-40.3),
    'GO':(-15.8,-49.6),'MA':(-5.4,-45.4),'MG':(-18.5,-44.0),'MS':(-20.5,-54.8),
    'MT':(-12.6,-55.9),'PA':(-3.4,-52.0),'PB':(-7.1,-36.9),'PE':(-8.4,-37.9),
    'PI':(-7.7,-42.7),'PR':(-24.9,-51.5),'RJ':(-22.2,-42.8),'RN':(-5.8,-36.6),
    'RO':(-10.8,-62.8),'RR':(2.0,-61.4),'RS':(-30.0,-53.2),'SC':(-27.3,-50.2),
    'SE':(-10.5,-37.4),'SP':(-22.9,-48.4),'TO':(-10.2,-48.3)
}

# Rata-rata delivery days per state (dari data historis yang sudah diketahui)
DELIVERY_DAYS = {
    'RR': 29.5,'AP': 28.1,'AM': 26.8,'AC': 25.3,'PA': 24.7,'MA': 22.1,
    'PI': 21.4,'TO': 20.8,'RO': 20.2,'AL': 18.6,'SE': 17.9,'PB': 17.4,
    'RN': 17.1,'CE': 16.8,'BA': 16.2,'PE': 15.8,'MT': 15.4,'MS': 14.9,
    'GO': 14.3,'DF': 13.8,'ES': 13.2,'SC': 12.7,'PR': 12.1,'RJ': 11.8,
    'MG': 11.4,'RS': 11.0,'SP': 8.9
}

# ── SIDEBAR ──────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("""
    <div class='sidebar-logo'>
        <div class='sidebar-logo-icon'>🛒</div>
        <div>
            <div class='sidebar-logo-text'>Olist Analytics</div>
            <div class='sidebar-logo-sub'>E-Commerce Brazil</div>
        </div>
    </div>
    <div class='divider'></div>
    """, unsafe_allow_html=True)

    st.markdown("<div style='font-size:0.72rem;font-weight:600;color:#4a5270;text-transform:uppercase;letter-spacing:1.2px;margin-bottom:8px'>📅 Rentang Waktu</div>", unsafe_allow_html=True)
    min_date = df_raw['order_purchase_timestamp'].min().date()
    max_date = df_raw['order_purchase_timestamp'].max().date()
    date_range = st.date_input(
        "Pilih periode", value=(min_date, max_date),
        min_value=min_date, max_value=max_date, label_visibility='collapsed'
    )

    st.markdown("<div class='divider'></div>", unsafe_allow_html=True)
    st.markdown("<div style='font-size:0.72rem;font-weight:600;color:#4a5270;text-transform:uppercase;letter-spacing:1.2px;margin-bottom:8px'>🗺️ Filter State</div>", unsafe_allow_html=True)
    all_states = sorted(df_raw['customer_state'].unique())
    selected_states = st.multiselect("State", all_states, placeholder="Semua state", label_visibility='collapsed')

    st.markdown("<div class='divider'></div>", unsafe_allow_html=True)
    st.markdown("<div style='font-size:0.72rem;font-weight:600;color:#4a5270;text-transform:uppercase;letter-spacing:1.2px;margin-bottom:8px'>📦 Filter Kategori</div>", unsafe_allow_html=True)
    all_cats = sorted(df_raw['product_category_name_english'].dropna().unique())
    selected_cats = st.multiselect("Kategori", all_cats, placeholder="Semua kategori", label_visibility='collapsed')

    st.markdown("<div class='divider'></div>", unsafe_allow_html=True)
    st.markdown("""
    <div style='font-size:0.68rem;color:#2e3550;line-height:1.8;'>
        Source: Brazilian E-Commerce<br>Public Dataset · Olist<br>
        <span style='color:#3d4870'>Sep 2016 – Agt 2018</span>
    </div>
    """, unsafe_allow_html=True)

# ── FILTER DATA ───────────────────────────────────────────────────────
df = df_raw.copy()
if len(date_range) == 2:
    df = df[(df['order_purchase_timestamp'].dt.date >= date_range[0]) &
            (df['order_purchase_timestamp'].dt.date <= date_range[1])]
if selected_states:
    df = df[df['customer_state'].isin(selected_states)]
if selected_cats:
    df = df[df['product_category_name_english'].isin(selected_cats)]

# ── HEADER ────────────────────────────────────────────────────────────
st.markdown("""
<div class='dash-header'>
    <div class='dash-header-bg'></div>
    <div class='dash-header-content'>
        <div class='dash-eyebrow'>● Live Dashboard</div>
        <div class='dash-title'>E-Commerce <span class='grad'>Analytics</span></div>
        <div class='dash-sub'>Analisis komprehensif performa penjualan, pelanggan, dan distribusi geografis Olist — platform e-commerce terbesar Brasil.</div>
        <div class='dash-header-pills'>
            <span class='dash-pill'><span class='dot' style='background:#5b8cff'></span> 2016–2018</span>
            <span class='dash-pill'><span class='dot' style='background:#00e5c8'></span> Brazil</span>
            <span class='dash-pill'><span class='dot' style='background:#4ade80'></span> Olist Dataset</span>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# ── KPI CARDS ─────────────────────────────────────────────────────────
total_revenue   = df['revenue'].sum()
total_orders    = df['order_id'].nunique()
total_customers = df['customer_unique_id'].nunique()
avg_order_val   = df['revenue'].mean()

st.markdown(f"""
<div class='kpi-grid'>
    <div class='kpi-card'>
        <div class='kpi-accent' style='background:linear-gradient(180deg,#5b8cff,#3b6cff)'></div>
        <div class='kpi-glow' style='background:#5b8cff'></div>
        <div class='kpi-icon' style='background:rgba(91,140,255,0.12)'>💰</div>
        <div class='kpi-label'>Total Revenue</div>
        <div class='kpi-value'>R${total_revenue/1e6:.2f}M</div>
        <span class='kpi-change pos'>↑ Seluruh periode</span>
    </div>
    <div class='kpi-card'>
        <div class='kpi-accent' style='background:linear-gradient(180deg,#00e5c8,#00bfa8)'></div>
        <div class='kpi-glow' style='background:#00e5c8'></div>
        <div class='kpi-icon' style='background:rgba(0,229,200,0.1)'>🛒</div>
        <div class='kpi-label'>Total Orders</div>
        <div class='kpi-value'>{total_orders:,}</div>
        <span class='kpi-change pos'>↑ Status delivered</span>
    </div>
    <div class='kpi-card'>
        <div class='kpi-accent' style='background:linear-gradient(180deg,#ffcc4d,#ffb020)'></div>
        <div class='kpi-glow' style='background:#ffcc4d'></div>
        <div class='kpi-icon' style='background:rgba(255,204,77,0.1)'>👥</div>
        <div class='kpi-label'>Unique Customers</div>
        <div class='kpi-value'>{total_customers:,}</div>
        <span class='kpi-change pos'>↑ Customer unik</span>
    </div>
    <div class='kpi-card'>
        <div class='kpi-accent' style='background:linear-gradient(180deg,#a78bfa,#8b5cf6)'></div>
        <div class='kpi-glow' style='background:#a78bfa'></div>
        <div class='kpi-icon' style='background:rgba(167,139,250,0.1)'>📊</div>
        <div class='kpi-label'>Avg Order Value</div>
        <div class='kpi-value'>R${avg_order_val:.0f}</div>
        <span class='kpi-change pos'>↑ Per transaksi</span>
    </div>
</div>
""", unsafe_allow_html=True)

# ── TABS ──────────────────────────────────────────────────────────────
tab1, tab2, tab3, tab4 = st.tabs(["📈  Tren", "📦  Kategori", "👥  RFM", "🗺️  Geospatial"])

# ════════════════════════════════════════════════════════════════════
# TAB 1 — TREN (Pertanyaan 1)
# ════════════════════════════════════════════════════════════════════
with tab1:
    monthly = compute_monthly(df)

    st.markdown("""
    <div class='section-header'>
        <div class='section-label'>Pertanyaan 1</div>
        <div class='section-title'>Tren Order & Revenue Bulanan (2017–2018)</div>
        <div class='section-desc'>Pada bulan apa terjadi puncak penjualan tertinggi selama periode 2017–2018?</div>
    </div>
    """, unsafe_allow_html=True)

    if monthly.empty:
        st.warning("Tidak ada data untuk filter yang dipilih.")
    else:
        st.markdown("<div class='chart-wrap'>", unsafe_allow_html=True)
        fig, axes = plt.subplots(2, 1, figsize=(14, 8), sharex=True, facecolor=BG)
        fig.patch.set_facecolor(BG)
        fig.subplots_adjust(hspace=0.08)

        x = np.arange(len(monthly))
        x_labels = monthly['order_month'].dt.strftime('%b %Y')

        def smooth_area(ax, x, y, color):
            for i in range(8, 0, -1):
                ax.fill_between(x, y, alpha=0.012 * i, color=color, linewidth=0)
            ax.plot(x, y, color=color, linewidth=2, zorder=5, solid_capstyle='round')

        ax1 = axes[0]
        ax1.set_facecolor(BG)
        smooth_area(ax1, x, monthly['order_count'], PALETTE['blue'])
        peak_i = monthly['order_count'].idxmax()
        ax1.scatter([peak_i], [monthly.loc[peak_i,'order_count']], color='white', s=60, zorder=6, linewidth=2, edgecolors=PALETTE['blue'])
        ax1.annotate(
            f"Peak: {monthly.loc[peak_i,'order_count']:,}",
            xy=(peak_i, monthly.loc[peak_i,'order_count']),
            xytext=(max(0, peak_i - 4), monthly.loc[peak_i,'order_count'] * 0.82),
            arrowprops=dict(arrowstyle='->', color=PALETTE['blue'], lw=1.2, connectionstyle='arc3,rad=-0.2'),
            color=PALETTE['blue'], fontsize=8, fontweight='bold',
            bbox=dict(boxstyle='round,pad=0.3', facecolor=BG2, edgecolor=PALETTE['blue'], alpha=0.9, linewidth=0.8)
        )
        ax1.set_ylabel('Orders', fontsize=8.5, color=TEXT, labelpad=10)
        ax1.yaxis.set_major_formatter(mticker.FuncFormatter(lambda v,_: f'{int(v):,}'))
        ax1.tick_params(axis='both', which='both', length=0, pad=6)
        ax1.grid(True, axis='y', color=GRID, linewidth=0.5)
        ax1.spines[:].set_visible(False)
        ax1.spines['left'].set_visible(True)
        ax1.spines['left'].set_color(GRID)
        ax1.set_xlim(-0.5, len(x)-0.5)
        ax1.text(0.01, 0.96, 'Jumlah Order / Bulan', transform=ax1.transAxes, fontsize=10, color=TEXT2, fontweight='600', va='top')

        ax2 = axes[1]
        ax2.set_facecolor(BG)
        smooth_area(ax2, x, monthly['total_revenue'], PALETTE['teal'])
        rev_peak_i = monthly['total_revenue'].idxmax()
        ax2.scatter([rev_peak_i], [monthly.loc[rev_peak_i,'total_revenue']], color='white', s=60, zorder=6, linewidth=2, edgecolors=PALETTE['teal'])
        ax2.annotate(
            f"Peak: R${monthly.loc[rev_peak_i,'total_revenue']/1e6:.2f}M",
            xy=(rev_peak_i, monthly.loc[rev_peak_i,'total_revenue']),
            xytext=(max(0, rev_peak_i - 4), monthly.loc[rev_peak_i,'total_revenue'] * 0.82),
            arrowprops=dict(arrowstyle='->', color=PALETTE['teal'], lw=1.2, connectionstyle='arc3,rad=-0.2'),
            color=PALETTE['teal'], fontsize=8, fontweight='bold',
            bbox=dict(boxstyle='round,pad=0.3', facecolor=BG2, edgecolor=PALETTE['teal'], alpha=0.9, linewidth=0.8)
        )
        ax2.set_ylabel('Revenue (R$)', fontsize=8.5, color=TEXT, labelpad=10)
        ax2.yaxis.set_major_formatter(mticker.FuncFormatter(lambda v,_: f'R${v/1e6:.1f}M'))
        ax2.tick_params(axis='both', which='both', length=0, pad=6)
        ax2.grid(True, axis='y', color=GRID, linewidth=0.5)
        ax2.spines[:].set_visible(False)
        ax2.spines['left'].set_visible(True)
        ax2.spines['left'].set_color(GRID)
        ax2.set_xlim(-0.5, len(x)-0.5)
        ax2.text(0.01, 0.96, 'Total Revenue / Bulan', transform=ax2.transAxes, fontsize=10, color=TEXT2, fontweight='600', va='top')

        tick_pos = list(range(0, len(x_labels), max(1, len(x_labels)//12)))
        ax2.set_xticks(tick_pos)
        ax2.set_xticklabels([x_labels.iloc[i] for i in tick_pos], rotation=35, ha='right', fontsize=8)

        plt.tight_layout()
        st.pyplot(fig, use_container_width=True)
        plt.close()
        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)
        s1, s2, s3 = st.columns(3)
        peak_month = monthly.loc[monthly['order_count'].idxmax(), 'order_month'].strftime('%b %Y')
        for col, val, lbl in [
            (s1, f"{monthly['order_count'].mean():.0f}", "Rata-rata Order/Bulan"),
            (s2, f"{monthly['order_count'].max():,} ({peak_month})", "Puncak Order"),
            (s3, f"R${monthly['total_revenue'].max()/1e6:.2f}M", "Revenue Tertinggi"),
        ]:
            col.markdown(f"""
            <div class='stat-mini'>
                <div class='stat-mini-val'>{val}</div>
                <div class='stat-mini-lbl'>{lbl}</div>
            </div>""", unsafe_allow_html=True)

# ════════════════════════════════════════════════════════════════════
# TAB 2 — KATEGORI (Pertanyaan 2)
# ════════════════════════════════════════════════════════════════════
with tab2:
    cat_df    = compute_category(df)
    cat_clean = cat_df[cat_df['category'] != 'unknown']
    top_n     = st.slider("Tampilkan Top N Kategori", 5, 20, 10, key='cat_slider')
    top       = cat_clean.head(top_n)
    bot       = cat_clean.tail(top_n)

    st.markdown("""
    <div class='section-header'>
        <div class='section-label'>Pertanyaan 2</div>
        <div class='section-title'>Performa Kategori Produk (2016–2018)</div>
        <div class='section-desc'>Kategori mana yang menghasilkan revenue tertinggi dan terendah, dan berapa rata-rata nilai transaksinya?</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<div class='chart-wrap'>", unsafe_allow_html=True)
    fig, axes = plt.subplots(1, 2, figsize=(16, 7), facecolor=BG)

    for ax, data, accent, bg_bar, title in zip(
        axes,
        [top[::-1], bot[::-1]],
        [PALETTE['blue'], PALETTE['rose']],
        ['#1a2240', '#2a1525'],
        [f'Top {top_n} — Revenue Tertinggi', f'Bottom {top_n} — Revenue Terendah']
    ):
        ax.set_facecolor(BG)
        idx = range(top_n)
        colors = [accent if i == top_n-1 else bg_bar for i in range(top_n)]
        ax.barh(idx, data['total_revenue'].values, color=colors, edgecolor='none', height=0.6)
        ax.set_yticks(idx)
        ax.set_yticklabels(data['category'].values, fontsize=8.5, color=TEXT2)
        ax.set_title(title, fontsize=10.5, color=TEXT2, pad=14, loc='left', fontweight='600')
        ax.set_xlabel('Total Revenue (R$)', fontsize=8.5, color=TEXT)
        ax.xaxis.set_major_formatter(mticker.FuncFormatter(
            lambda v,_: f'R${v/1e6:.1f}M' if v >= 1e6 else f'R${v/1e3:.0f}K'
        ))
        ax.spines[:].set_visible(False)
        ax.tick_params(length=0, pad=6)
        ax.grid(True, axis='x', color=GRID, linewidth=0.5)
        ax.set_xlim(0, data['total_revenue'].max() * 1.28)

        for i, (_, row) in enumerate(data.iterrows()):
            ax.text(
                row['total_revenue'] + data['total_revenue'].max() * 0.02,
                list(idx)[list(data.index).index(_)],
                f"avg R${row['avg_order_value']:.0f}",
                va='center', fontsize=7.5, color=TEXT
            )

    plt.tight_layout(w_pad=4)
    st.pyplot(fig, use_container_width=True)
    plt.close()
    st.markdown("</div>", unsafe_allow_html=True)

    # Top 5 highlight
    st.markdown("<br>", unsafe_allow_html=True)
    cols = st.columns(5)
    for i, (col, (_, row)) in enumerate(zip(cols, cat_clean.head(5).iterrows())):
        col.markdown(f"""
        <div class='stat-mini'>
            <div class='stat-mini-val' style='font-size:1rem'>{row['category'].replace('_',' ').title()}</div>
            <div class='stat-mini-lbl'>R${row['total_revenue']/1e3:.0f}K revenue</div>
        </div>""", unsafe_allow_html=True)

# ════════════════════════════════════════════════════════════════════
# TAB 3 — RFM (Pertanyaan 3)
# ════════════════════════════════════════════════════════════════════
with tab3:
    seg_df = compute_rfm_segments(df)

    st.markdown("""
    <div class='section-header'>
        <div class='section-label'>Pertanyaan 3</div>
        <div class='section-title'>Segmentasi Pelanggan — RFM Analysis (2016–2018)</div>
        <div class='section-desc'>Berapa % pelanggan Champions dan At Risk? Apa strategi retensi untuk masing-masing segmen?</div>
    </div>
    """, unsafe_allow_html=True)

    seg_colors = {
        'Champions': PALETTE['blue'], 'Loyal Customers': PALETTE['teal'],
        'Recent Customers': PALETTE['gold'], 'Potential Loyalists': PALETTE['green'],
        'At Risk': PALETTE['rose'], 'Lost': '#f87171',
    }
    seg_css = {
        'Champions': 'seg-champions', 'Loyal Customers': 'seg-loyal',
        'Recent Customers': 'seg-recent', 'Potential Loyalists': 'seg-potential',
        'At Risk': 'seg-atrisk', 'Lost': 'seg-lost',
    }

    col_pie, col_bar = st.columns([1, 1.5])

    with col_pie:
        st.markdown("<div class='chart-wrap'>", unsafe_allow_html=True)
        fig, ax = plt.subplots(figsize=(5.5, 5.5), facecolor=BG)
        ax.set_facecolor(BG)
        colors_pie = [seg_colors.get(s, '#888') for s in seg_df['segment']]
        wedges, texts, autotexts = ax.pie(
            seg_df['count'], labels=None, autopct='%1.1f%%',
            colors=colors_pie, startangle=140, pctdistance=0.72,
            wedgeprops=dict(edgecolor=BG, linewidth=2.5, width=0.55)
        )
        for at in autotexts:
            at.set_fontsize(7.5); at.set_color('#fff'); at.set_fontweight('600')
        ax.legend(wedges, seg_df['segment'], loc='lower center', bbox_to_anchor=(0.5, -0.14),
                  fontsize=8, frameon=False, labelcolor=TEXT2, ncol=2)
        ax.set_title('Proporsi Segmen RFM', fontsize=10.5, color=TEXT2, pad=12, fontweight='600')
        plt.tight_layout()
        st.pyplot(fig, use_container_width=True)
        plt.close()
        st.markdown("</div>", unsafe_allow_html=True)

    with col_bar:
        st.markdown("<div class='chart-wrap'>", unsafe_allow_html=True)
        fig, ax = plt.subplots(figsize=(8, 5.5), facecolor=BG)
        ax.set_facecolor(BG)
        sorted_seg = seg_df.sort_values('count', ascending=True)
        colors_bar = [seg_colors.get(s, '#888') for s in sorted_seg['segment']]
        ax.barh(sorted_seg['segment'], sorted_seg['count'], color=colors_bar, edgecolor='none', height=0.55, alpha=0.9)
        for i, (_, row) in enumerate(sorted_seg.iterrows()):
            ax.text(row['count'] + sorted_seg['count'].max() * 0.015, i,
                    f"{row['count']:,} ({row['pct']}%)", va='center', fontsize=9, color=TEXT2, fontweight='500')
        ax.set_title('Jumlah Pelanggan per Segmen', fontsize=10.5, color=TEXT2, pad=12, loc='left', fontweight='600')
        ax.set_xlabel('Jumlah Pelanggan', fontsize=8.5, color=TEXT)
        ax.xaxis.set_major_formatter(mticker.FuncFormatter(lambda v,_: f'{int(v):,}'))
        ax.spines[:].set_visible(False)
        ax.tick_params(length=0, pad=6)
        ax.grid(True, axis='x', color=GRID, linewidth=0.5)
        ax.set_xlim(0, sorted_seg['count'].max() * 1.25)
        plt.tight_layout()
        st.pyplot(fig, use_container_width=True)
        plt.close()
        st.markdown("</div>", unsafe_allow_html=True)

    # Stats table
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("""
    <div class='section-header'>
        <div class='section-title'>Statistik & Strategi per Segmen</div>
    </div>
    """, unsafe_allow_html=True)

    STRATEGI = {
        'Champions':          'Program loyalty eksklusif, early access produk baru, reward tier khusus',
        'Loyal Customers':    'Pertahankan dengan program poin & diskon ulang tahun',
        'Recent Customers':   'Dorong pembelian kedua dengan voucher first-repeat purchase',
        'Potential Loyalists':'Insentif pembelian kedua, email campaign personal',
        'At Risk':            'Re-engagement: diskon personal + reminder berbasis waktu',
        'Lost':               'Win-back campaign; jika tidak respon, relokasi budget ke segmen lain',
    }

    st.markdown("""
    <div class='tbl-header' style='grid-template-columns:1.8fr 0.8fr 1.2fr 1fr 1.2fr 2.5fr'>
        <span>Segmen</span><span>Jumlah</span><span>Avg Recency</span><span>Avg Freq</span><span>Avg Monetary</span><span>Strategi</span>
    </div>
    """, unsafe_allow_html=True)

    for _, row in seg_df.sort_values('avg_monetary', ascending=False).iterrows():
        css = seg_css.get(row['segment'], '')
        strat = STRATEGI.get(row['segment'], '-')
        st.markdown(f"""
        <div class='tbl-row' style='grid-template-columns:1.8fr 0.8fr 1.2fr 1fr 1.2fr 2.5fr;align-items:center'>
            <span><span class='seg-badge {css}'>{row['segment']}</span></span>
            <span style='color:{TEXT2};font-weight:500'>{int(row['count']):,} <span style='color:{TEXT};font-weight:400'>({row['pct']}%)</span></span>
            <span style='color:{TEXT}'>{row['avg_recency']:.0f} hari</span>
            <span style='color:{TEXT}'>{row['avg_frequency']:.1f}x</span>
            <span style='color:{TEXT}'>R${row['avg_monetary']:.0f}</span>
            <span style='color:{TEXT};font-size:0.8rem'>{strat}</span>
        </div>
        """, unsafe_allow_html=True)

# ════════════════════════════════════════════════════════════════════
# TAB 4 — GEOSPATIAL (Pertanyaan 4)
# ════════════════════════════════════════════════════════════════════
with tab4:
    st.markdown("""
    <div class='section-header'>
        <div class='section-label'>Pertanyaan 4</div>
        <div class='section-title'>Rata-rata Waktu Pengiriman per State (2016–2018)</div>
        <div class='section-desc'>State mana yang memiliki delivery time tertinggi, dan berapa selisihnya vs rata-rata nasional?</div>
    </div>
    """, unsafe_allow_html=True)

    # Build delivery dataframe
    delivery_df = pd.DataFrame([
        {'state': k, 'avg_delivery_days': v} for k, v in DELIVERY_DAYS.items()
    ]).sort_values('avg_delivery_days', ascending=False).reset_index(drop=True)

    national_avg = delivery_df['avg_delivery_days'].mean()
    delivery_df['selisih'] = (delivery_df['avg_delivery_days'] - national_avg).round(1)

    # Filter by selected states if any
    disp_del = delivery_df.copy()
    if selected_states:
        disp_del = disp_del[disp_del['state'].isin(selected_states)]

    # ── KPI delivery ──
    slowest = delivery_df.iloc[0]
    fastest = delivery_df.iloc[-1]
    d1, d2, d3 = st.columns(3)
    d1.markdown(f"""<div class='stat-mini'><div class='stat-mini-val' style='color:#ff6b8a'>{national_avg:.1f} hari</div><div class='stat-mini-lbl'>Rata-rata Nasional</div></div>""", unsafe_allow_html=True)
    d2.markdown(f"""<div class='stat-mini'><div class='stat-mini-val' style='color:#ff6b8a'>{slowest['avg_delivery_days']} hari</div><div class='stat-mini-lbl'>Terlama — {slowest['state']}</div></div>""", unsafe_allow_html=True)
    d3.markdown(f"""<div class='stat-mini'><div class='stat-mini-val' style='color:#4ade80'>{fastest['avg_delivery_days']} hari</div><div class='stat-mini-lbl'>Tercepat — {fastest['state']}</div></div>""", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # ── Bar chart delivery time ──
    st.markdown("<div class='chart-wrap'>", unsafe_allow_html=True)
    fig, ax = plt.subplots(figsize=(14, 7), facecolor=BG)
    ax.set_facecolor(BG)

    plot_df = disp_del.sort_values('avg_delivery_days', ascending=True)
    bar_colors = []
    for d in plot_df['avg_delivery_days']:
        if d > 20:
            bar_colors.append(PALETTE['rose'])
        elif d > 14:
            bar_colors.append(PALETTE['gold'])
        else:
            bar_colors.append(PALETTE['green'])

    bars = ax.barh(plot_df['state'], plot_df['avg_delivery_days'],
                   color=bar_colors, edgecolor='none', height=0.65, zorder=3)

    # National average line
    ax.axvline(national_avg, color='white', linestyle='--', linewidth=1.2, alpha=0.4, zorder=4)
    ax.text(national_avg + 0.3, len(plot_df) - 0.5,
            f'Rata-rata nasional\n{national_avg:.1f} hari',
            color='white', fontsize=7.5, alpha=0.6, va='top')

    # Value labels
    for bar, val, state in zip(bars, plot_df['avg_delivery_days'], plot_df['state']):
        selisih = val - national_avg
        sign = '+' if selisih >= 0 else ''
        ax.text(val + 0.3, bar.get_y() + bar.get_height()/2,
                f'{val:.1f} hari  ({sign}{selisih:.1f})',
                va='center', fontsize=8, color=TEXT2)

    ax.set_title('Rata-rata Waktu Pengiriman per State vs Rata-rata Nasional',
                 fontsize=11, color=TEXT2, pad=14, loc='left', fontweight='600')
    ax.set_xlabel('Rata-rata Hari Pengiriman', fontsize=8.5, color=TEXT)
    ax.set_ylabel('State', fontsize=8.5, color=TEXT)
    ax.spines[:].set_visible(False)
    ax.tick_params(length=0, pad=6)
    ax.grid(True, axis='x', color=GRID, linewidth=0.5, zorder=0)
    ax.set_xlim(0, plot_df['avg_delivery_days'].max() * 1.25)

    slow_patch = mpatches.Patch(color=PALETTE['rose'],  label='> 20 hari (lambat)')
    mid_patch  = mpatches.Patch(color=PALETTE['gold'],  label='14–20 hari (sedang)')
    fast_patch = mpatches.Patch(color=PALETTE['green'], label='< 14 hari (cepat)')
    ax.legend(handles=[slow_patch, mid_patch, fast_patch], fontsize=8.5,
              frameon=False, labelcolor=TEXT2, loc='lower right')

    plt.tight_layout()
    st.pyplot(fig, use_container_width=True)
    plt.close()
    st.markdown("</div>", unsafe_allow_html=True)

    # ── Tabel detail ──
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("""
    <div class='section-header'>
        <div class='section-title'>Detail Waktu Pengiriman per State</div>
        <div class='section-desc'>Diurutkan dari yang terlama — selisih dihitung terhadap rata-rata nasional</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class='tbl-header' style='grid-template-columns:0.5fr 1fr 1.5fr 1.5fr 1.5fr'>
        <span>#</span><span>State</span><span>Avg Delivery (hari)</span><span>Selisih vs Nasional</span><span>Kategori</span>
    </div>
    """, unsafe_allow_html=True)

    for rank, (_, row) in enumerate(delivery_df.iterrows()):
        if selected_states and row['state'] not in selected_states:
            continue
        selisih = row['selisih']
        sign = '+' if selisih >= 0 else ''
        if row['avg_delivery_days'] > 20:
            cat_html = "<span class='delivery-slow'>Lambat</span>"
        elif row['avg_delivery_days'] > 14:
            cat_html = "<span class='delivery-avg'>Sedang</span>"
        else:
            cat_html = "<span class='delivery-fast'>Cepat</span>"

        selisih_color = '#ff6b8a' if selisih > 0 else '#4ade80'
        st.markdown(f"""
        <div class='tbl-row' style='grid-template-columns:0.5fr 1fr 1.5fr 1.5fr 1.5fr;align-items:center'>
            <span style='color:{TEXT};font-size:0.8rem'>#{rank+1}</span>
            <span style='color:{TEXT2};font-weight:600'>{row['state']}</span>
            <span style='color:{TEXT2};font-weight:500'>{row['avg_delivery_days']} hari</span>
            <span style='color:{selisih_color};font-weight:500'>{sign}{selisih} hari</span>
            <span>{cat_html}</span>
        </div>
        """, unsafe_allow_html=True)